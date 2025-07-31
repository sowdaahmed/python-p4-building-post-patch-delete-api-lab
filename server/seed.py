from app import app
from models import db, Bakery, BakedGood

with app.app_context():
    BakedGood.query.delete()
    Bakery.query.delete()

    bakery1 = Bakery(name="Sunrise Bakery")
    bakery2 = Bakery(name="Moonlight Bakery")

    db.session.add_all([bakery1, bakery2])
    db.session.commit()

    bg1 = BakedGood(name="Croissant", price=3.50, bakery_id=bakery1.id)
    bg2 = BakedGood(name="Sourdough", price=4.25, bakery_id=bakery1.id)
    bg3 = BakedGood(name="Bagel", price=2.00, bakery_id=bakery2.id)

    db.session.add_all([bg1, bg2, bg3])
    db.session.commit()

    print("🌱 Database seeded!")
