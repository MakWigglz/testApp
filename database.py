import sqlite3

def create_database():
    conn = sqlite3.connect('encyclopedia.db')
    c = conn.cursor()
    
    # Create topics table
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY,
                  main_topic TEXT NOT NULL,
                  subtopic TEXT NOT NULL,
                  content TEXT,
                  UNIQUE(main_topic, subtopic))''')
    
    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect('encyclopedia.db')
    c = conn.cursor()
    
    topics_data = [
        ('Science', 'Physics', 'Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.'),
        ('Science', 'Chemistry', 'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.'),
        ('Science', 'Biology', 'Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.'),
        ('Science', 'Mathematics', 'Mathematics is the study of quantity, structure, space, and change.'),
        ('History', 'Ancient civilizations', 'Ancient civilizations refers to complex societies with urban development, social stratification, a form of government, and symbolic systems of communication.'),
        ('History', 'Modern history', 'Modern history, also referred to as the modern period or the modern era, is the historiographical approach to the timeframe after the post-classical era.'),
        ('Art', 'Painting', 'Painting is the practice of applying paint, pigment, color or other medium to a solid surface.'),
        ('Art', 'Sculpture', 'Sculpture is the branch of the visual arts that operates in three dimensions.'),
        ('Art', 'Architecture', 'Architecture is both the process and the product of planning, designing, and constructing buildings or other structures.'),
        ('Technology', 'Computer Science', 'Computer science is the study of computation, automation, and information.'),
        ('Technology', 'Artificial Intelligence', 'Artificial intelligence is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans.'),
        ('Technology', 'Robotics', 'Robotics is an interdisciplinary field that integrates computer science and engineering.'),
        ('Philosophy', 'Ethics', 'Ethics or moral philosophy is a branch of philosophy that involves systematizing, defending, and recommending concepts of right and wrong behavior.'),
        ('Philosophy', 'Metaphysics', 'Metaphysics is the branch of philosophy that examines the fundamental nature of reality.'),
        ('Philosophy', 'Epistemology', 'Epistemology is the branch of philosophy concerned with knowledge.')
    ]
    
    c.executemany('INSERT OR REPLACE INTO topics (main_topic, subtopic, content) VALUES (?, ?, ?)', topics_data)
    
    conn.commit()
    conn.close()

def add_new_content(main_topic, subtopic, content):
    conn = sqlite3.connect('encyclopedia.db')
    c = conn.cursor()
    
    c.execute('INSERT OR REPLACE INTO topics (main_topic, subtopic, content) VALUES (?, ?, ?)', 
              (main_topic, subtopic, content))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    insert_sample_data()
    
    # Adding new content
    add_new_content('Science', 'Computer Science', 'Computer science is the study of computation, automation, and information. It explores various aspects of computer programming, algorithms, data structures, and computer hardware.')
    add_new_content('Technology', 'Blockchain', 'Blockchain is a decentralized, distributed ledger that records transactions in a secure and transparent manner. It uses cryptography to ensure the integrity and security of the data. It relies on the public to ensure transparency. Blockchain is created by computer code.') 
    add_new_content('Technology', 'Quantum Computing', 'Quantum computing is a type of computation that uses quantum bits, or qubits, to represent information. Unlike classical bits, which can only be in either a 0 or 1, qubits can exist in a superposition of both states simultaneously. Quantum computers can perform complex calculations much faster than classical computers.')
    add_new_content('Art', 'Literature', 'Literature is a broad term that encompasses various forms of written expression, including verbal, written, and visual. Literature can be divided into various genres. Some common literary genres include poetry, prose, short stories, novels, essays, and essays.')
    add_new_content('Geography', 'Mountains', 'Mountains are natural landform features that form a high-altitude structure, often with rounded bases. They are often characterized by steep slopes, dense forests, and elevated peaks. Some of the most famous mountains in the world include Mount Everest, the highest peak on Earth, and Mount Kilimanjaro,')
    add_new_content('Geography', 'Climate change', 'Climate change refers to the long-term alteration of Earths climate patterns due to human activities, including deforestation, agriculture, industrialization, and natural disasters. Climate change can lead to increased temperatures, extreme weather events, and loss of biodiversity.')
    add_new_content('Geography', 'Human Geography', '...or anthropogeography is the branch of geography which studies spatial relationships between human communities, cultures, economies, and their interactions with the environment, examples of which include urban sprawl and urban redevelopment.[1] It analyzes spatial interdependencies between social interactions and the environment through qualitative and quantitative methods.[2][3] This multidisciplinary approach draws from sociology, anthropology, economics, and environmental science, contributing to a comprehensive understanding of the intricate connections that shape lived spaces. The Royal Geographical Society was founded in England in 1830.[5] The first professor of geography in the United Kingdom was appointed in 1883,[6] and the first major geographical intellect to emerge in the UK was Halford John Mackinder, appointed professor of geography at the London School of Economics in 1922. The National Geographic Society was founded in the United States in 1888 and began publication of the National Geographic magazine which became, and continues to be, a great popularizer of geographic information. The society has long supported geographic research and education on geographical topics. The Association of American Geographers was founded in 1904 and was renamed the American Association of Geographers in 2016 to better reflect the increasingly international character of its membership. One of the first examples of geographic methods being used for purposes other than to describe and theorize the physical properties of the earth is John Snows map of the 1854 Broad Street cholera outbreak. Though Snow was primarily a physician and a pioneer of epidemiology rather than a geographer, his map is probably one of the earliest examples of health geography.')