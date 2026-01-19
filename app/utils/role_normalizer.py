def normalize_role(role: str) -> str:
    if not role:
        return ""

    role = role.lower().strip()

    mapping = {        
        "data analyst": "Data Analyst",
        "data analytics": "Data Analyst",
        "data scientist": "Data Scientist",

        "backend developer": "Backend Developer",
        "python developer": "Backend Developer",
        "frontend developer": "Frontend Developer",
        "front end developer": "Frontend Developer",
        "web developer": "Frontend Developer",
        "ui ux designer": "Frontend Developer",
        "ui/ux designer": "Frontend Developer",
        "user experience": "Frontend Developer",
        "user interface": "Frontend Developer",
        "software developer": "Software Developer",
        "devops developer": "DevOps Developer",
        "cloud developer": "Cloud Developer",
        "mobile developer": "Mobile Developer",
        "game developer": "Game Developer",

        "machine learning": "AI/ML Engineer",
        "ai ml engineer": "AI/ML Engineer",
        "ai/ml engineer": "AI/ML Engineer",
        "artificial intelligence engineer": "AI/ML Engineer",

        "ai researcher": "AI Researcher",
        "research scientist ai": "AI Researcher",

        "database engineer": "Database Engineer",
        "dbms": "Database Engineer",
        "sql developer": "Database Engineer",

        "cyber security analyst": "Cyber Security Analyst",
        "security analyst": "Cyber Security Analyst",
        "information security": "Cyber Security Analyst",

        "qa engineer": "QA Engineer",
        "test engineer": "QA Engineer",
        "software tester": "QA Engineer",
    }

    for key in mapping:
        if key in role:
            return mapping[key]

    return role.title()
