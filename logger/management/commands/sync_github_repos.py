from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from logger.models import Repository, Language

class Command(BaseCommand):
    help = 'Syncs GitHub repository data into our Django app'

    def handle(self, *args, **options):
        # Use your personal access token and set the appropriate headers
        headers = {
            'Authorization': f'token {settings.GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json',
        }

        # Make a request to get your repositories
        response = requests.get('https://api.github.com/user/repos', headers=headers)

        if response.status_code == 200:
            for repo_data in response.json():
                # Extract necessary data
                name = repo_data['name']
                # You might need additional API calls to get build/deployment statuses
                version_number = repo_data.get('default_branch')  # Often 'master' or 'main'
                languages_url = repo_data['languages_url']

                # Get languages for the repo
                languages_response = requests.get(languages_url, headers=headers)
                if languages_response.status_code == 200:
                    languages_data = languages_response.json()
                    languages = [Language.objects.get_or_create(name=lang)[0] for lang in languages_data.keys()]

                # Create or update the repository in your database
                repo, created = Repository.objects.get_or_create(name=name)
                repo.version_number = version_number
                # repo.build_status = '...' # Set your build status here
                # repo.deployment_status = '...' # Set your deployment status here
                repo.save()
                repo.languages.set(languages)

                self.stdout.write(self.style.SUCCESS(f'Successfully updated "{name}"'))

        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve repositories'))
