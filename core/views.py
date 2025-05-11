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
    if request.method == 'POST':
        form = GuestUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user, created = GuestUser.objects.get_or_create(name=name)

            # Save user's name in session
            request.session['guest_name'] = user.name
            request.session['guest_id'] = user.id

            # Redirect to challenge list
            return redirect('challenge_list')
    else:
        form = GuestUserForm()
    
    return render(request, 'core/choose_access.html', {'form': form})


def challenge_entry(request):
    if request.user.is_authenticated:
        return redirect('challenge_list') 
    return render(request, 'choose_access.html') 


def challenge_detail(request, lang_slug, challenge_slug):
     
    challenge = get_object_or_404(
        CodeChallenge,
        language__slug=lang_slug,
        slug=challenge_slug
    )
    if request.method == 'POST':
        pass 
    else:
         form = ChallengeSubmissionForm(num_blanks=challenge.get_number_of_blanks())
         context = {'challenge': challenge, 'form': form}
         return render(request, 'core/challenge_detail.html', context)

def challenge_list(request):
    """Displays a list of available challenges."""
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
        'guest_name': guest_name,  # Add guest name to context
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