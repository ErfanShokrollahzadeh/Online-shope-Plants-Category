from django.shortcuts import render

def about_view(request):
    team_members = [
        {
            'name': 'John Doe',
            'position': 'CEO & Founder',
            'image': 'https://randomuser.me/api/portraits/men/1.jpg',
            'description': 'Plant enthusiast with 15 years of experience in botanical gardens.',
        },
        {
            'name': 'Jane Smith',
            'position': 'Head Botanist',
            'image': 'https://randomuser.me/api/portraits/women/1.jpg',
            'description': 'Expert in tropical plants and indoor gardening.',
        },
        {
            'name': 'Mike Johnson',
            'position': 'Customer Experience',
            'image': 'https://randomuser.me/api/portraits/men/2.jpg',
            'description': 'Dedicated to ensuring the best service for plant lovers.',
        },
    ]
    
    milestones = [
        {'year': '2018', 'title': 'Founded', 'description': 'Started with a small garden shop'},
        {'year': '2020', 'title': 'Online Launch', 'description': 'Expanded to e-commerce'},
        {'year': '2022', 'title': 'National Coverage', 'description': 'Now delivering across the country'},
        {'year': '2024', 'title': 'Going Global', 'description': 'International shipping available'},
    ]
    
    return render(request, 'about_module/about.html', {
        'team_members': team_members,
        'milestones': milestones,
    })
