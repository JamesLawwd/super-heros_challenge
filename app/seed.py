import random
from models import db, Power, Hero, HeroPower
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

# This line is necessary to create an application context
with app.app_context():
    print("🦸‍♂️ Seeding superpowers...")
    superpowers_data = [
        {"name": "super strength", "description": "grants the wielder superhuman strength"},
        {"name": "flight", "description": "bestows the ability to soar through the skies at supersonic speed"},
        {"name": "superhuman senses", "description": "enables the wielder to use senses at a superhuman level"},
        {"name": "elasticity", "description": "allows stretching the human body to extreme lengths"}
    ]

    for superpower_data in superpowers_data:
        superpower = Power(**superpower_data)
        db.session.add(superpower)

    db.session.commit()

    print("🦸‍♂️ Seeding superheroes...")
    superheroes_data = [
        {"name": "Peter Parker", "super_name": "Spider-Man"},
        {"name": "Bruce Wayne", "super_name": "Batman"},
        {"name": "Clark Kent", "super_name": "Superman"},
        {"name": "Diana Prince", "super_name": "Wonder Woman"},
        {"name": "Barry Allen", "super_name": "The Flash"},
        {"name": "Tony Stark", "super_name": "Iron Man"},
        {"name": "Natasha Romanoff", "super_name": "Black Widow"},
        {"name": "Thor Odinson", "super_name": "Thor"},
        {"name": "Steve Rogers", "super_name": "Captain America"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"}
    ]

    for superhero_data in superheroes_data:
        superhero = Hero(**superhero_data)
        db.session.add(superhero)

    db.session.commit()

    print("🦸‍♂️ Adding superpowers to superheroes...")
    strengths = ["Strong", "Weak", "Average"]
    for superhero in Hero.query.all():
        for _ in range(random.randint(1, 3)):
            superpower = Power.query.get(random.randint(1, len(superpowers_data)))
            superhero_power = HeroPower(hero_id=superhero.id, power_id=superpower.id, strength=random.choice(strengths))
            db.session.add(superhero_power)

    db.session.commit()

    print("🦸‍♂️ Done seeding!")
