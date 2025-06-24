from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import CodeChallenge, ProgrammingLanguage, Tag
from .forms import ChallengeSubmissionForm
from django.shortcuts import render, redirect
from core.models import CodeChallenge
from .forms import GuestUserForm
from .models import GuestUser

def index(request):

    context = {
        'page_title': 'Welcome to notacoder!',
    }
    return render(request, 'core/index.html', context)

def choose_access(request):
    # ... (the start of your view remains the same) ...

    if request.method == 'POST':
        form = GuestUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            magic_word = form.cleaned_data['magic_word']

            try:
                user = GuestUser.objects.get(name=name)
                if user.magic_word == magic_word:
                    # SUCCESSFUL LOGIN
                    request.session['guest_user_id'] = user.id
                    messages.success(request, f"Welcome back, {user.name}!")
                    
                    # *** THE FIX IS HERE ***
                    # Redirect to the 'challenge_detail' URL, passing 'challenge_id'.
                    return redirect('challenge_list')
                else:
                    # FAILED LOGIN
                    messages.error(request, "That's not the right Magic Word for that name.")
                    return redirect('choose_access')

            except GuestUser.DoesNotExist:
                # NEW USER SIGN UP
                user = GuestUser.objects.create(
                    name=name,
                    magic_word=magic_word,
                    current_challenge=1
                )
                request.session['guest_user_id'] = user.id

                # *** THE FIX IS HERE TOO ***
                # Redirect to the 'challenge_detail' URL, passing 'challenge_id'.
                return redirect('challenge_list')
    else:
        form = GuestUserForm()

    return render(request, 'core/choose_access.html', {'form': form})


def user_dashboard(request):
    # THE FIX: Get the correct key from the session.
    user_id = request.session.get('guest_user_id')
    
    # If the user ID isn't in the session, they are not logged in.
    # Send them to the login page.
    if not user_id:
        return redirect('choose_access')

    # THE FIX: Find the user by their unique ID.
    user = get_object_or_404(GuestUser, id=user_id)
    
    # NOW you have the correct user object, and you can access their progress.
    # For example, to send them to the right challenge:
    # return redirect('challenge_page', challenge_number=user.current_challenge)

    # For now, we'll just render the dashboard with the user's info.
    return render(request, 'core/user_dashboard.html', {'user': user})

def challenge_entry(request):
    if request.user.is_authenticated:
        return redirect('challenge_list')
    return render(request, 'core/challenge_entry.html')
 


def challenge_detail(request, lang_slug, challenge_slug, challenge_id):
     
    challenge = get_object_or_404(
        CodeChallenge, id=challenge_id,
        language__slug=lang_slug,
        slug=challenge_slug,
    )
    if request.method == 'POST':
        pass 
    else:
         form = ChallengeSubmissionForm(num_blanks=challenge.get_number_of_blanks())
         context = {'challenge': challenge, 'form': form}
         return render(request, 'core/challenge_detail.html', context)

def challenge_list(request):
    """Displays a list of available challenges."""
    user = None
    user_id = request.session.get('guest_user_id')
    if user_id:
        try:
            # This line re-assigns the 'user' variable if a user is found.
            user = GuestUser.objects.get(id=user_id) 
        except GuestUser.DoesNotExist:
            # If the ID is bad, the 'user' variable just remains None.
            pass

    guest_name = request.session.get('guest_name')  # Get user's name from session

    challenges = CodeChallenge.objects.all()
    languages = ProgrammingLanguage.objects.all()
    tags = Tag.objects.all()

    lang_filter = request.GET.get('language')
    tag_filter = request.GET.get('tag')

    if lang_filter:
        challenges = challenges.filter(language__slug=lang_filter)
    if tag_filter:
        challenges = challenges.filter(tags__slug=tag_filter)

    context = {
        'challenges': challenges,
        'languages': languages,
        'tags': tags,
        'selected_language': lang_filter,
        'selected_tag': tag_filter,
        'guest_name': guest_name,
        'user': user,
    }
    return render(request, 'core/challenge_list.html', context)


# @login_required
def challenge_detail(request, lang_slug, challenge_slug):
    """Displays a single challenge and handles submission."""
    challenge = get_object_or_404(
        CodeChallenge,
        language__slug=lang_slug,
        slug=challenge_slug
    )
    num_blanks = challenge.get_number_of_blanks()
    has_submitted = False
    is_correct = None
    submitted_answers = None
    full_code = None

    if request.method == 'POST':
        form = ChallengeSubmissionForm(request.POST, num_blanks=num_blanks)
        has_submitted = True

        if form.is_valid():
            submitted_answers = form.get_ordered_answers()
            is_correct = challenge.check_submission(submitted_answers)

            if is_correct:
                messages.success(request, f'🎉 Correct! You earned {challenge.points_reward} points!')
                full_code = challenge.construct_full_code(submitted_answers)
            else:
                messages.error(request, '❌ Not quite right. Try again!')
        else:
            messages.error(request, "Please fill in all the blanks.")
    else:
        form = ChallengeSubmissionForm(num_blanks=num_blanks)

    context = {
        'challenge': challenge,
        'form': form,
        'has_submitted': has_submitted,
        'is_correct': is_correct,
        'submitted_answers': submitted_answers,
        'full_code': full_code
    }

    return render(request, 'core/challenge_detail.html', context)