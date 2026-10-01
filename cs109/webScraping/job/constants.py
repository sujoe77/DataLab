IGNORE_SAME_POSITION_FOR_DAYS = 15
OUTPUT_FOLDER = "/home/zhou/git/gitlab/notes/job/data/"

KEYWORD_DIC_ALL = {
        "java": 5, "python": 5,  "rust": 3, "golang": 5, "scala": 3, "c#": 5, "kotlin": 3, "jvm": 5, "Spring": 5, "kafka": 3, "kubernetes": 3, "redis": 3,
        "AI": 5, "Machine Learning": 5, "LLM": 5, "ML": 5,
        "software engineer": 10, "developer": 10, "backend developer": 5, "programmer": 5, "udvikler": 5,  "backend engineer": 5, "fullstack developer": 5,
        "data engineer": 5, "data scientist": 5, 
        "architect": 5, "Tech Lead": 5, "principal engineer": 5, "lead developer": 5, "IT Lead": 5,  
        "finance it": 5, "fintech": 5, "banking it": 5, "trading": 5, "payment": 5, "chinese": 2, "China": 2
    }

KEYWORD_DIC_TECH = { 
            "java": 5, "jvm": 5, "Spring": 5,
            "Kafka": 5, "kotlin": 5, "scala": 5, "python": 5, "rust": 5, "golang": 5, "c#": 5, "AI": 5
        }

KEYWORD_DIC_JAVA_TECH = { 
            "java": 10, "jvm": 10, "Spring": 5, "Kotlin": 5, "Scala": 5
        }

KEYWORD_DIC_POS = { 
            "architect": 5, "Tech Lead": 5, "principal engineer": 5, "lead developer": 5, "IT Lead": 5
        }

KEYWORD_DIC_POS_BASIC = { 
            "developer": 10, "engineer": 10, "programmer": 10, "software": 10
        }

KEYWORD_DIC_JAVA_TECH_1 = { 
            "java": 10
        }

KEYWORD_DIC_JAVA_TECH_2 = { 
            "java": 2
        }

KEYWORD_DIC_ONE_WORD = { 
            "Backend Engineer": 5
        }

EXECLUDE_TITLE = ["student", "test", "frontend", 
                      #"c#", "udvikler", 
                      "android", 
                      #"analyst", 
                      #"devops", "security", 
                      "sale", 
                      #"Javascript", 
                      "QA",
                      #".NET",
                      #"javascript",
                      #"microsoft",
                      "php"
                     ]
EXECLUDE_COMPANY = [
                    #"prodata", 
                    "SoftNice"]