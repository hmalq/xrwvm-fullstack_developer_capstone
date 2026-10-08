from .models import CarMake, CarModel


def initiate():
    makes = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Great cars. German technology"),
        ("Audi", "Great cars. German technology"),
        ("Kia", "Great cars. Korean technology"),
        ("Toyota", "Great cars. Japanese technology"),
    ]
    made = [CarMake.objects.create(name=n, description=d) for n, d in makes]

    models_data = [
        ("Pathfinder", "SUV", 0), ("Qashqai", "SUV", 0), ("XTRAIL", "SUV", 0),
        ("A-Class", "SUV", 1), ("C-Class", "SEDAN", 1), ("E-Class", "SEDAN", 1),
        ("A4", "SEDAN", 2), ("A5", "SEDAN", 2), ("A6", "SEDAN", 2),
        ("Sorrento", "SUV", 3), ("Carnival", "WAGON", 3), ("Cerato", "SEDAN", 3),
        ("Corolla", "SEDAN", 4), ("Camry", "SEDAN", 4), ("Kluger", "SUV", 4),
    ]
    for name, car_type, idx in models_data:
        CarModel.objects.create(
            car_make=made[idx],
            dealer_id=1,
            name=name,
            type=car_type,
            year=2023,
        )
