import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SkillEdge.settings')
django.setup()

from Community.models import Topic

# List of default topics with descriptions
default_topics = [
    {
        'name': 'Programming',
        'description': 'Discussions about programming languages, coding challenges, and software development',
        'icon': 'code'
    },
    {
        'name': 'Data Science',
        'description': 'Topics related to data analysis, machine learning, and artificial intelligence',
        'icon': 'graph-up'
    },
    {
        'name': 'Web Development',
        'description': 'Frontend, backend, and full-stack web development discussions',
        'icon': 'globe'
    },
    {
        'name': 'Career Advice',
        'description': 'Career guidance, job hunting tips, and professional development',
        'icon': 'briefcase'
    },
    {
        'name': 'Learning Resources',
        'description': 'Share and discuss learning materials, courses, and tutorials',
        'icon': 'book'
    },
    {
        'name': 'Projects',
        'description': 'Project ideas, showcases, and collaboration opportunities',
        'icon': 'folder'
    },
    {
        'name': 'Tech News',
        'description': 'Latest updates in technology and industry trends',
        'icon': 'newspaper'
    }
]

def create_topics():
    for topic_data in default_topics:
        Topic.objects.get_or_create(
            name=topic_data['name'],
            defaults={
                'description': topic_data['description'],
                'icon': topic_data['icon']
            }
        )
        print(f"Created/Updated topic: {topic_data['name']}")

if __name__ == '__main__':
    print("Creating default topics...")
    create_topics()
    print("Done!") 