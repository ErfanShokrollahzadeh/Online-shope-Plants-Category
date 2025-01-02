from django.shortcuts import render

def blog_list_view(request):
    blog_posts = [
        {
            'title': 'Essential Tips for Indoor Plant Care',
            'category': 'Plant Care',
            'image': 'https://images.unsplash.com/photo-1545241047-6083a3684587',
            'excerpt': 'Learn the basics of keeping your indoor plants healthy and thriving with proper watering, lighting, and care techniques.',
            'author': 'Jane Smith',
            'date': '2024-01-15',
            'read_time': '5 min read',
            'likes': 124,
            'comments': 45
        },
        {
            'title': 'Top 10 Air-Purifying Plants',
            'category': 'Plant Types',
            'image': 'https://images.unsplash.com/photo-1512428813834-c702c7702b78',  # Updated image URL
            'excerpt': 'Discover the best plants for improving your indoor air quality, including Spider Plants, Snake Plants, and Peace Lilies.',
            'author': 'John Doe',
            'date': '2024-01-10',
            'read_time': '8 min read',
            'likes': 256,
            'comments': 89
        },
        {
            'title': 'Succulent Care for Beginners',
            'category': 'Plant Care',
            'image': 'https://images.unsplash.com/photo-1459411552884-841db9b3cc2a',
            'excerpt': 'Everything you need to know about caring for succulents, from watering schedules to soil requirements.',
            'author': 'Maria Garcia',
            'date': '2024-01-08',
            'read_time': '6 min read',
            'likes': 189,
            'comments': 67
        },
        {
            'title': 'Creating a Beautiful Herb Garden',
            'category': 'Gardening',
            'image': 'https://images.unsplash.com/photo-1466692476868-aef1dfb1e735',
            'excerpt': 'Step-by-step guide to starting your own herb garden, perfect for fresh cooking ingredients right at home.',
            'author': 'Alex Chen',
            'date': '2024-01-05',
            'read_time': '10 min read',
            'likes': 312,
            'comments': 94
        },
        {
            'title': 'Rare Houseplants Worth Collecting',
            'category': 'Plant Types',
            'image': 'https://images.unsplash.com/photo-1463936575829-25148e1db1b8',
            'excerpt': 'Explore unique and rare houseplants that can add exotic beauty to your indoor plant collection.',
            'author': 'Sarah Johnson',
            'date': '2024-01-03',
            'read_time': '7 min read',
            'likes': 423,
            'comments': 156
        },
        {
            'title': 'Seasonal Plant Care Guide',
            'category': 'Plant Care',
            'image': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b',
            'excerpt': 'How to adjust your plant care routine through different seasons for optimal growth and health.',
            'author': 'Mike Wilson',
            'date': '2024-01-01',
            'read_time': '9 min read',
            'likes': 267,
            'comments': 78
        },
        {
            'title': 'Modern Plant Styling Tips',
            'category': 'Design',
            'image': 'https://images.unsplash.com/photo-1501004318641-b39e6451bec6',
            'excerpt': 'Creative ideas for incorporating plants into your home décor for a modern, fresh look.',
            'author': 'Emma Davis',
            'date': '2023-12-28',
            'read_time': '6 min read',
            'likes': 345,
            'comments': 112
        },
        {
            'title': 'Propagation Techniques',
            'category': 'Plant Care',
            'image': 'https://images.unsplash.com/photo-1446071103084-c257b5f70672',
            'excerpt': 'Learn different methods to propagate your plants and expand your indoor garden for free.',
            'author': 'Tom Brown',
            'date': '2023-12-25',
            'read_time': '8 min read',
            'likes': 289,
            'comments': 93
        },
        {
            'title': 'Pet-Friendly Plant Guide',
            'category': 'Safety',
            'image': 'https://images.unsplash.com/photo-1491147334573-44cbb4602074',
            'excerpt': 'Complete guide to plants that are safe for homes with cats, dogs, and other pets.',
            'author': 'Lisa Cooper',
            'date': '2023-12-22',
            'read_time': '7 min read',
            'likes': 534,
            'comments': 167
        }
    ]
    
    return render(request, 'blog_module/blog_list.html', {'blog_posts': blog_posts})
