from faker import Faker


class FakeGenerator:
    faker = Faker()

    @classmethod
    def name(cls):
        return cls.faker.name()

    @classethod
    def password(cls):
        return cls.faker.password()

    fake = FakeGenerator()
