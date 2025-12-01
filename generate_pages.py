import os

# College Data
colleges = [
    {
        "id": "brahmanbaria",
        "name": "Brahmanbaria Medical College",
        "location": "Brahmanbaria",
        "established": "2013",
        "type": "Private",
        "affiliation": "University of Chittagong",
        "recognition": "NMC, WHO, BMDC, MCI",
        "official_fee": "$38,000",
        "first_payment": "$14,000",
        "hostel_mess": "Included (Both)",
        "total_cost": "$38,000",
        "rating": "4.2/5",
        "badge": "All Inclusive",
        "description": "Brahmanbaria Medical College is known for its affordable all-inclusive package. It is the only college where both hostel and food costs are included in the tuition fee, making it an excellent choice for budget-conscious students.",
        "highlights": [
            "Food and Hostel included in the package",
            "Modern hospital with 250+ beds",
            "Located close to Agartala border",
            "High patient flow for clinical practice"
        ]
    },
    {
        "id": "army-jashore",
        "name": "Army Medical College Jashore",
        "location": "Jashore",
        "established": "2014",
        "type": "Army/Public-Private",
        "affiliation": "Bangladesh University of Professionals (BUP)",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$45,000",
        "first_payment": "$20,500",
        "hostel_mess": "Included (Mess+Laundry)",
        "total_cost": "$45,000",
        "rating": "4.5/5",
        "badge": "Army College",
        "description": "Army Medical College Jashore offers a disciplined environment with top-notch facilities. Being an army college, it ensures safety, punctuality, and high academic standards.",
        "highlights": [
            "Run by Bangladesh Army",
            "Secure and disciplined campus",
            "Internship in Combined Military Hospital (CMH)",
            "5 meals a day included"
        ]
    },
    {
        "id": "northeast",
        "name": "North East Medical College",
        "location": "Sylhet",
        "established": "1998",
        "type": "Private",
        "affiliation": "Sylhet Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$42,500",
        "first_payment": "$12,500",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$45,500",
        "rating": "4.1/5",
        "badge": "ROI Focused",
        "description": "North East Medical College is one of the premier institutions in Sylhet. It is unique for offering a salary to foreign students during their internship, significantly improving the ROI.",
        "highlights": [
            "Paid internship for foreign students",
            "Large 800-bed hospital",
            "Scenic location in Sylhet",
            "Excellent passing rate"
        ]
    },
    {
        "id": "president",
        "name": "President Abdul Hamid Medical College",
        "location": "Kishoreganj",
        "established": "2013",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$36,000",
        "first_payment": "$13,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$39,600",
        "rating": "4.0/5",
        "badge": "Low Cost",
        "description": "Named after the former President of Bangladesh, this college offers a great balance of quality education and affordability.",
        "highlights": [
            "Very affordable tuition fees",
            "Modern infrastructure",
            "Good clinical exposure",
            "Experienced faculty"
        ]
    },
    {
        "id": "akij",
        "name": "Ad-din Akij Medical College",
        "location": "Khulna",
        "established": "2013",
        "type": "Private",
        "affiliation": "Rajshahi Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$33,000",
        "first_payment": "$13,000",
        "hostel_mess": "Extra: $60/mo (Food+Util)",
        "total_cost": "$36,600",
        "rating": "3.9/5",
        "badge": "Budget Friendly",
        "description": "Part of the renowned Ad-din foundation, this college focuses on serving humanity. It offers one of the lowest tuition fees in the country.",
        "highlights": [
            "Extremely low tuition fee",
            "Charitable hospital setup",
            "Focus on community medicine",
            "Separate campus for boys"
        ]
    },
    {
        "id": "sakina",
        "name": "Ad-din Sakina Women's Medical College",
        "location": "Jashore",
        "established": "2011",
        "type": "Private (Women)",
        "affiliation": "Rajshahi Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$33,000",
        "first_payment": "$13,000",
        "hostel_mess": "Extra: $140/mo (Total)",
        "total_cost": "$41,400",
        "rating": "4.3/5",
        "badge": "Women Only",
        "description": "A top choice for female students, ensuring a secure and conservative environment. The college has excellent results and a strict academic calendar.",
        "highlights": [
            "Women-only secure campus",
            "High patient flow",
            "Strict discipline and safety",
            "Affordable package"
        ]
    },
    {
        "id": "momin",
        "name": "Ad-din Momin Medical College",
        "location": "Dhaka",
        "established": "2013",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$35,000",
        "first_payment": "$18,000",
        "hostel_mess": "Extra: Util $25/mo",
        "total_cost": "$40,000",
        "rating": "4.0/5",
        "badge": "Near Dhaka",
        "description": "Located just on the outskirts of Dhaka, it offers the advantage of the capital city's connectivity with a peaceful campus environment.",
        "highlights": [
            "Proximity to Dhaka",
            "Managed by Ad-din foundation",
            "Good hostel facilities",
            "Modern labs and library"
        ]
    },
    {
        "id": "city",
        "name": "City Medical College",
        "location": "Gazipur",
        "established": "2011",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$40,000",
        "first_payment": "$17,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$43,600",
        "rating": "4.1/5",
        "badge": "High Tech",
        "description": "City Medical College is known for its huge 300-bed hospital and high patient flow, located in the industrial hub of Gazipur.",
        "highlights": [
            "Large hospital capacity",
            "High patient inflow",
            "Modern campus infrastructure",
            "Experienced teaching staff"
        ]
    },
    {
        "id": "us-bangla",
        "name": "US-Bangla Medical College",
        "location": "Narayanganj",
        "established": "2013",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$40,000",
        "first_payment": "$15,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$43,600",
        "rating": "4.2/5",
        "badge": "Green Campus",
        "description": "Run by the US-Bangla group, this college boasts a sprawling green campus and state-of-the-art infrastructure.",
        "highlights": [
            "Beautiful eco-friendly campus",
            "Backed by US-Bangla Group",
            "Well-equipped laboratories",
            "Comfortable hostel accommodation"
        ]
    },
    {
        "id": "central",
        "name": "Central Medical College",
        "location": "Cumilla",
        "established": "2005",
        "type": "Private",
        "affiliation": "Chittagong Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$41,000",
        "first_payment": "$16,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$44,600",
        "rating": "4.0/5",
        "badge": "Established",
        "description": "One of the older private medical colleges in the Cumilla region, known for its academic consistency.",
        "highlights": [
            "Experienced faculty",
            "Stable academic environment",
            "Good clinical rotation",
            "Library with vast resources"
        ]
    },
    {
        "id": "samorita",
        "name": "MH Samorita Medical College",
        "location": "Dhaka",
        "established": "2010",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$42,000",
        "first_payment": "$18,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$45,600",
        "rating": "4.3/5",
        "badge": "City Center",
        "description": "Located in the heart of Dhaka city, providing students with exposure to a wide variety of medical cases and urban life.",
        "highlights": [
            "Central Dhaka location",
            "High patient diversity",
            "Associated with Samorita Hospital",
            "Vibrant student life"
        ]
    },
    {
        "id": "sylhet-women",
        "name": "Sylhet Women's Medical College",
        "location": "Sylhet",
        "established": "2005",
        "type": "Private (Women)",
        "affiliation": "Sylhet Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$42,000",
        "first_payment": "$15,000",
        "hostel_mess": "Extra: Food ~$65/mo",
        "total_cost": "$46,000",
        "rating": "4.4/5",
        "badge": "Premium Women",
        "description": "A premier institution for women in Sylhet, known for its excellent results and secure, supportive environment.",
        "highlights": [
            "Dedicated to women's education",
            "Top-tier faculty",
            "Excellent PLAB/USMLE support",
            "Modern hostel facilities"
        ]
    },
    {
        "id": "addin-women",
        "name": "Ad-din Women's Medical College",
        "location": "Dhaka",
        "established": "2008",
        "type": "Private (Women)",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$43,000",
        "first_payment": "$23,000",
        "hostel_mess": "Extra: Util $30/mo",
        "total_cost": "$48,000",
        "rating": "4.5/5",
        "badge": "Top Choice",
        "description": "One of the most reputed women's medical colleges in Bangladesh. It maintains high standards of discipline and academics.",
        "highlights": [
            "Located in Moghbazar, Dhaka",
            "Very high patient flow",
            "Strict academic discipline",
            "Excellent postgraduate options"
        ]
    },
    {
        "id": "jalalabad",
        "name": "Jalalabad Ragib-Rabeya Medical College",
        "location": "Sylhet",
        "established": "1995",
        "type": "Private",
        "affiliation": "Sylhet Medical University",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$44,000",
        "first_payment": "$20,000",
        "hostel_mess": "Hostel Inc. / Food Incidental",
        "total_cost": "$47,600",
        "rating": "4.2/5",
        "badge": "Reputed",
        "description": "A vast campus spread over a large area, it is one of the oldest and most respected private medical colleges in Sylhet.",
        "highlights": [
            "Large 900-bed hospital",
            "Spacious campus",
            "International student community",
            "Experienced professors"
        ]
    },
    {
        "id": "dhaka-central",
        "name": "Dhaka Central International Medical College",
        "location": "Dhaka",
        "established": "2010",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$44,500",
        "first_payment": "$16,600",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$48,100",
        "rating": "4.1/5",
        "badge": "Modern",
        "description": "A modern medical college located in Shyamoli, Dhaka, committed to producing competent medical professionals.",
        "highlights": [
            "Modern teaching aids",
            "Air-conditioned classrooms",
            "Good location",
            "Supportive faculty"
        ]
    },
    {
        "id": "universal",
        "name": "Universal Medical College",
        "location": "Dhaka",
        "established": "2013",
        "type": "Private",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$45,000",
        "first_payment": "$20,000",
        "hostel_mess": "Hostel Inc. / Food Self",
        "total_cost": "$48,600",
        "rating": "4.0/5",
        "badge": "Clinical Focus",
        "description": "Formerly known as Ayesha Memorial Medical College, it has a strong focus on clinical skills and patient care.",
        "highlights": [
            "Renowned hospital",
            "Focus on practical skills",
            "Cultural activities",
            "Alumni network"
        ]
    },
    {
        "id": "women-hospital",
        "name": "Medical College for Women & Hospital",
        "location": "Dhaka",
        "established": "1992",
        "type": "Private (Women)",
        "affiliation": "University of Dhaka",
        "recognition": "NMC, WHO, BMDC",
        "official_fee": "$47,000",
        "first_payment": "$15,000",
        "hostel_mess": "Hostel Rent Extra?",
        "total_cost": "$50,000+",
        "rating": "4.6/5",
        "badge": "Prestigious",
        "description": "The first private medical college exclusively for women in Bangladesh. It holds a legacy of excellence.",
        "highlights": [
            "Pioneer in women's medical education",
            "Two campuses in Uttara",
            "Global alumni network",
            "Top-notch academics"
        ]
    }
]

# Template for the college details page
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - MBBS Bangladesh</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}

        :root {{
            --primary: #1a73e8;
            --secondary: #34a853;
            --accent: #fbbc05;
            --dark: #202124;
            --light: #f8f9fa;
            --gray: #5f6368;
        }}

        body {{
            background-color: #f5f7fa;
            color: var(--dark);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .container {{
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        /* Header Styles */
        header {{
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}

        .header-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }}

        .logo {{
            display: flex;
            align-items: center;
        }}

        .logo i {{
            font-size: 28px;
            color: var(--primary);
            margin-right: 10px;
        }}

        .logo h1 {{
            font-size: 24px;
            color: var(--dark);
        }}

        .logo span {{
            color: var(--primary);
        }}

        nav ul {{
            display: flex;
            list-style: none;
        }}

        nav ul li {{
            margin-left: 25px;
        }}

        nav ul li a {{
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s;
        }}

        nav ul li a:hover {{
            color: var(--primary);
        }}

        .auth-buttons button {{
            padding: 8px 20px;
            border-radius: 4px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
        }}

        .login {{
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            margin-right: 10px;
        }}

        .login:hover {{
             background: rgba(26, 115, 232, 0.1);
        }}

        .register {{
            background: var(--primary);
            border: 1px solid var(--primary);
            color: white;
        }}

        .register:hover {{
            background: #0d62d9;
        }}

        /* Detail Hero Section */
        .college-hero {{
            background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%);
            color: white;
            padding: 60px 0;
            position: relative;
            overflow: hidden;
        }}

        .college-hero-content {{
            position: relative;
            z-index: 2;
        }}

        .college-title {{
            font-size: 42px;
            margin-bottom: 15px;
        }}

        .college-meta {{
            display: flex;
            gap: 20px;
            font-size: 16px;
            opacity: 0.9;
        }}

        .college-meta span i {{
            margin-right: 5px;
        }}

        .college-badge-large {{
            display: inline-block;
            background: var(--accent);
            color: var(--dark);
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: 600;
            margin-bottom: 15px;
        }}

        /* Carousel Styles */
        .carousel-container {{
            margin-top: 40px;
            width: 100%;
            height: 400px; /* Adjust height as needed */
            overflow: hidden;
            position: relative;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            background: #fff;
        }}

        .college-carousel {{
            display: flex;
            height: 100%;
            animation: carouselScroll 20s linear infinite;
        }}

        .college-carousel img {{
            height: 100%;
            width: auto; /* Maintains aspect ratio */
            min-width: 600px; /* Ensure images have width */
            object-fit: cover;
            flex-shrink: 0;
        }}

        @keyframes carouselScroll {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }} /* Move half way (assuming duplicated set) */
        }}

        /* Main Content */
        .college-main {{
            padding: 60px 0;
            background: white;
        }}

        .content-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 40px;
        }}

        .overview-card {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 15px rgba(0,0,0,0.05);
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid #eee;
        }}

        .overview-card h3 {{
            font-size: 24px;
            margin-bottom: 20px;
            color: var(--primary);
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 10px;
        }}

        .info-table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .info-table tr {{
            border-bottom: 1px solid #f0f0f0;
        }}

        .info-table tr:last-child {{
            border-bottom: none;
        }}

        .info-table td {{
            padding: 15px 0;
        }}

        .info-table td:first-child {{
            font-weight: 600;
            width: 40%;
            color: var(--gray);
        }}

        .highlights-list {{
            list-style: none;
        }}

        .highlights-list li {{
            margin-bottom: 12px;
            position: relative;
            padding-left: 25px;
        }}

        .highlights-list li::before {{
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--secondary);
            font-weight: bold;
        }}

        /* Sidebar */
        .fee-card {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            padding: 30px;
            position: sticky;
            top: 20px;
            border-top: 5px solid var(--secondary);
        }}

        .fee-header {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .fee-amount {{
            font-size: 36px;
            font-weight: 700;
            color: var(--secondary);
        }}

        .fee-label {{
            color: var(--gray);
            font-size: 14px;
        }}

        .fee-details {{
            margin-bottom: 25px;
        }}

        .fee-item {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            font-size: 15px;
        }}

        .fee-item.total {{
            font-weight: 700;
            border-top: 1px solid #eee;
            padding-top: 10px;
            margin-top: 10px;
            font-size: 18px;
        }}

        .action-buttons {{
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}

        .btn {{
            width: 100%;
            padding: 12px;
            border-radius: 5px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
            font-size: 16px;
        }}

        .btn-compare {{
            background: var(--secondary);
            color: white;
        }}

        .btn-compare:hover {{
            background: #2c8e47;
        }}

        .btn-contact {{
            background: var(--primary);
            color: white;
        }}

        .btn-contact:hover {{
            background: #0d62d9;
        }}

        .btn-brochure {{
            background: white;
            border: 1px solid var(--primary);
            color: var(--primary);
        }}

        .btn-brochure:hover {{
            background: #f0f7ff;
        }}

        /* Footer */
        footer {{
            background: var(--dark);
            color: white;
            padding: 60px 0 20px;
            margin-top: 60px;
        }}

        .footer-content {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }}

        .footer-column h3 {{
            font-size: 20px;
            margin-bottom: 20px;
            position: relative;
        }}

        .footer-column h3::after {{
            content: '';
            position: absolute;
            left: 0;
            bottom: -8px;
            width: 40px;
            height: 3px;
            background: var(--primary);
        }}

        .footer-column ul {{
            list-style: none;
        }}

        .footer-column ul li {{
            margin-bottom: 10px;
        }}

        .footer-column ul li a {{
            color: #bdc1c6;
            text-decoration: none;
            transition: color 0.3s;
        }}

        .footer-column ul li a:hover {{
            color: white;
        }}

        .copyright {{
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #bdc1c6;
            font-size: 14px;
        }}

        /* Floating Cart for Consistency */
        .floating-cart {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.15);
            z-index: 1000;
            width: 350px;
            max-width: 90vw;
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s ease;
            border: 1px solid #e0e0e0;
        }}

        .floating-cart.active {{
            transform: translateY(0);
            opacity: 1;
        }}

        .cart-header {{
            background: var(--primary);
            color: white;
            padding: 15px 20px;
            border-radius: 10px 10px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .cart-count {{
            background: var(--accent);
            color: var(--dark);
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }}

        .cart-content {{
            padding: 15px 20px;
            max-height: 300px;
            overflow-y: auto;
        }}

        .cart-items {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .cart-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid #f0f0f0;
        }}

        .cart-item-name {{
            font-size: 14px;
        }}

        .cart-item-remove {{
            background: none;
            border: none;
            color: #dc3545;
            cursor: pointer;
            font-size: 16px;
        }}

        .cart-actions {{
            padding: 15px 20px;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 10px;
        }}

        .cart-actions .btn {{
            flex: 1;
            padding: 8px;
            font-size: 14px;
        }}

        .btn-success {{
            background: var(--secondary);
            color: white;
        }}

        .btn-danger {{
            background: #dc3545;
            color: white;
        }}

        @media (max-width: 768px) {{
            .content-grid {{
                grid-template-columns: 1fr;
            }}

            .college-hero {{
                padding: 40px 0;
            }}

            .college-title {{
                font-size: 32px;
            }}

            .college-carousel {{
                animation-duration: 10s;
            }}

            .college-carousel img {{
                min-width: 100vw;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo">
                <i class="fas fa-stethoscope"></i>
                <h1>MBBS<span>Bangladesh</span></h1>
            </div>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="all-colleges.html">Colleges</a></li>
                    <li><a href="#">Fees</a></li>
                    <li><a href="comparison.html">Comparison</a></li>
                    <li><a href="#">Admission</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
            <div class="auth-buttons">
                <button class="login">Login</button>
                <button class="register">Register</button>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="college-hero">
        <div class="container">
            <div class="college-hero-content">
                {badge_html}
                <h1 class="college-title">{name}</h1>
                <div class="college-meta">
                    <span><i class="fas fa-map-marker-alt"></i> {location}</span>
                    <span><i class="fas fa-university"></i> Established: {established}</span>
                    <span><i class="fas fa-star"></i> {rating}</span>
                </div>
            </div>

            <!-- Carousel Placeholder -->
            <div class="carousel-container">
                <div class="college-carousel">
                    <!-- Placeholder images - 5 images doubled for infinite loop -->
                    <img src="https://via.placeholder.com/800x400/1a73e8/ffffff?text={encoded_name}+View+1" alt="{name} Campus">
                    <img src="https://via.placeholder.com/800x400/34a853/ffffff?text={encoded_name}+Labs" alt="{name} Labs">
                    <img src="https://via.placeholder.com/800x400/fbbc05/202124?text={encoded_name}+Classrooms" alt="{name} Classroom">
                    <img src="https://via.placeholder.com/800x400/ea4335/ffffff?text={encoded_name}+Hostel" alt="{name} Hostel">
                    <img src="https://via.placeholder.com/800x400/1a73e8/ffffff?text={encoded_name}+Hospital" alt="{name} Hospital">

                    <!-- Duplicate for smooth loop -->
                    <img src="https://via.placeholder.com/800x400/1a73e8/ffffff?text={encoded_name}+View+1" alt="{name} Campus">
                    <img src="https://via.placeholder.com/800x400/34a853/ffffff?text={encoded_name}+Labs" alt="{name} Labs">
                    <img src="https://via.placeholder.com/800x400/fbbc05/202124?text={encoded_name}+Classrooms" alt="{name} Classroom">
                    <img src="https://via.placeholder.com/800x400/ea4335/ffffff?text={encoded_name}+Hostel" alt="{name} Hostel">
                    <img src="https://via.placeholder.com/800x400/1a73e8/ffffff?text={encoded_name}+Hospital" alt="{name} Hospital">
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="college-main">
        <div class="container">
            <div class="content-grid">
                <!-- Left Column -->
                <div class="main-info">
                    <div class="overview-card">
                        <h3>About the College</h3>
                        <p>{description}</p>
                    </div>

                    <div class="overview-card">
                        <h3>Key Highlights</h3>
                        <ul class="highlights-list">
                            {highlights_html}
                        </ul>
                    </div>

                    <div class="overview-card">
                        <h3>Quick Information</h3>
                        <table class="info-table">
                            <tr>
                                <td>College Type</td>
                                <td>{type}</td>
                            </tr>
                            <tr>
                                <td>Affiliation</td>
                                <td>{affiliation}</td>
                            </tr>
                            <tr>
                                <td>Recognized By</td>
                                <td>{recognition}</td>
                            </tr>
                            <tr>
                                <td>Hostel & Mess</td>
                                <td>{hostel_mess}</td>
                            </tr>
                        </table>
                    </div>
                </div>

                <!-- Right Column (Sidebar) -->
                <div class="sidebar">
                    <div class="fee-card">
                        <div class="fee-header">
                            <span class="fee-label">Total Course Fee</span>
                            <div class="fee-amount">{total_cost}</div>
                        </div>
                        <div class="fee-details">
                            <div class="fee-item">
                                <span>Official Package</span>
                                <span>{official_fee}</span>
                            </div>
                            <div class="fee-item">
                                <span>First Payment</span>
                                <span>{first_payment}</span>
                            </div>
                            <div class="fee-item total">
                                <span>Est. Total Cost</span>
                                <span>{total_cost}</span>
                            </div>
                        </div>
                        <div class="action-buttons">
                            <button class="btn btn-compare" id="addCompareBtn" onclick="toggleCollegeInCart('{id}', '{name}')">Add to Compare</button>
                            <button class="btn btn-contact">Contact for Admission</button>
                            <button class="btn btn-brochure">Download Brochure</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>MBBS Bangladesh</h3>
                    <p>Your complete guide to pursuing MBBS in Bangladesh. We provide accurate information on medical colleges, fees, admission process, and more.</p>
                </div>
                <div class="footer-column">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="all-colleges.html">Medical Colleges</a></li>
                        <li><a href="#">Fee Structure</a></li>
                        <li><a href="#">Admission Process</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Contact Us</h3>
                    <ul>
                        <li><i class="fas fa-map-marker-alt"></i> Dhaka, Bangladesh</li>
                        <li><i class="fas fa-phone"></i> +880 1234 567890</li>
                        <li><i class="fas fa-envelope"></i> info@mbbscolleges.com</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2023 MBBS Bangladesh. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Floating Comparison Cart -->
    <div class="floating-cart" id="floatingCart">
        <div class="cart-header">
            <h3>Comparison Cart</h3>
            <span class="cart-count" id="cartCount">0</span>
        </div>
        <div class="cart-content">
            <div class="cart-items" id="cartItems">
                <div class="empty-cart-message">No colleges added to comparison</div>
            </div>
        </div>
        <div class="cart-actions">
            <button class="btn btn-success" id="compareBtn" disabled onclick="compareColleges()">Compare (0)</button>
            <button class="btn btn-danger" onclick="clearCart()">Clear</button>
        </div>
    </div>

    <script>
        // Shared Cart Logic
        let comparisonCart = [];
        const collegeId = "{id}";
        const collegeName = "{name}";

        document.addEventListener('DOMContentLoaded', function() {{
            // Load cart
            const savedCart = localStorage.getItem('comparisonColleges');
            if (savedCart) {{
                comparisonCart = JSON.parse(savedCart);
            }}

            updateCartUI();
            updateButtonState();
        }});

        function toggleCollegeInCart(id, name) {{
            if (comparisonCart.includes(id)) {{
                // Remove
                comparisonCart = comparisonCart.filter(item => item !== id);
            }} else {{
                // Add
                if (comparisonCart.length >= 2) {{
                    alert('You can only compare 2 colleges at a time.');
                    return;
                }}
                comparisonCart.push(id);
            }}

            localStorage.setItem('comparisonColleges', JSON.stringify(comparisonCart));
            updateCartUI();
            updateButtonState();
        }}

        function removeFromCart(id) {{
            comparisonCart = comparisonCart.filter(item => item !== id);
            localStorage.setItem('comparisonColleges', JSON.stringify(comparisonCart));
            updateCartUI();
            updateButtonState();
        }}

        function clearCart() {{
            comparisonCart = [];
            localStorage.setItem('comparisonColleges', JSON.stringify(comparisonCart));
            updateCartUI();
            updateButtonState();
        }}

        function updateCartUI() {{
            const cartElement = document.getElementById('floatingCart');
            const cartCount = document.getElementById('cartCount');
            const cartItems = document.getElementById('cartItems');
            const compareBtn = document.getElementById('compareBtn');

            cartCount.textContent = comparisonCart.length;
            compareBtn.textContent = `Compare (${{comparisonCart.length}})`;
            compareBtn.disabled = comparisonCart.length < 2;

            cartItems.innerHTML = '';

            if (comparisonCart.length === 0) {{
                cartItems.innerHTML = '<div class="empty-cart-message">No colleges added to comparison</div>';
                cartElement.classList.remove('active');
            }} else {{
                comparisonCart.forEach(id => {{
                    // Note: In a real app we'd look up name by ID, but here we might only know current page's name
                    // For now, we will try to handle it simply.
                    // To fully support names of *other* colleges, we'd need a global lookup object
                    // or store objects {{id, name}} in localStorage instead of just IDs.
                    // For this static demo, we will just show the ID or "College" if name unknown.

                    let name = id === collegeId ? collegeName : id; // Simple fallback

                    // Better approach: fetch name from localStorage if we stored objects,
                    // but we stuck to the existing pattern of storing IDs.
                    // We can accept this limitation for the generated pages for now.

                    const cartItem = document.createElement('div');
                    cartItem.className = 'cart-item';
                    cartItem.innerHTML = `
                        <span class="cart-item-name">${{name}}</span>
                        <button class="cart-item-remove" onclick="removeFromCart('${{id}}')">&times;</button>
                    `;
                    cartItems.appendChild(cartItem);
                }});
                cartElement.classList.add('active');
            }}
        }}

        function updateButtonState() {{
            const btn = document.getElementById('addCompareBtn');
            if (comparisonCart.includes(collegeId)) {{
                btn.textContent = '✓ Added to Compare';
                btn.classList.add('btn-success');
                btn.classList.remove('btn-compare');
            }} else {{
                btn.textContent = 'Add to Compare';
                btn.classList.add('btn-compare');
                btn.classList.remove('btn-success');
            }}
        }}

        function compareColleges() {{
            if (comparisonCart.length !== 2) {{
                alert('Please select exactly 2 colleges to compare.');
                return;
            }}
            window.location.href = 'comparison.html';
        }}
    </script>
</body>
</html>
"""

import urllib.parse

def generate_pages():
    for college in colleges:
        # Prepare data
        badge_html = f'<div class="college-badge-large">{college["badge"]}</div>' if college["badge"] else ""
        highlights_html = "\n".join([f'<li>{h}</li>' for h in college["highlights"]])
        encoded_name = urllib.parse.quote(college["name"])

        # Fill template
        html = template.format(
            id=college["id"],
            name=college["name"],
            location=college["location"],
            established=college["established"],
            type=college["type"],
            affiliation=college["affiliation"],
            recognition=college["recognition"],
            official_fee=college["official_fee"],
            first_payment=college["first_payment"],
            hostel_mess=college["hostel_mess"],
            total_cost=college["total_cost"],
            rating=college["rating"],
            description=college["description"],
            badge_html=badge_html,
            highlights_html=highlights_html,
            encoded_name=encoded_name
        )

        # Write file
        filename = f"{college['id']}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_pages()
