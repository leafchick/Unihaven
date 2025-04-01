from django.test import TestCase
from .models import CustomerUser, Reservations, Accommodation, Admin
from django.utils import timezone
from datetime import timedelta

class CustomerUserTestCase(TestCase):
    def setUp(self):
        """Create test data"""
        self.customer = CustomerUser.objects.create(
            name="BingZhang Lu",
            email="lubingzhang@hku.com",
            phone="1234567890"
        )

    def test_create_customer_user(self):
        """Test creating a CustomerUser instance"""

        self.assertEqual(self.customer.name, "BingZhang Lu")
        self.assertEqual(self.customer.email, "lubingzhang@hku.com")
        self.assertIsNotNone(self.customer.created_at)



class ReservationsTestCase(TestCase):
    def setUp(self):
        """Create test data"""
        self.customer = CustomerUser.objects.create(
            name="BingZhang Lu",
            email="lubingzhang@hku.com",
            phone="1234567890"
        )
        self.accommodation = Accommodation.objects.create(
            type="Single Room",
            period_of_availability="2023-06-01 to 2023-12-31",
            number_of_beds=1,
            number_of_bedrooms=1,
            room_id=101,
            price=100.00,
            distance=5.0
        )
        self.reservation = Reservations.objects.create(
            customer=self.customer,
            accommodation=self.accommodation,
            room_id=101,
            check_in_date=timezone.now().date(),
            check_out_date=timezone.now().date() + timedelta(days=3),
            rate_number=4.5
        )

    def test_create_reservation(self):
        """Test creating a Reservation instance"""

        self.assertEqual(self.reservation.customer, self.customer)
        self.assertEqual(self.reservation.accommodation, self.accommodation)
        self.assertEqual(self.reservation.room_id, 101)
        self.assertEqual(self.reservation.rate_number, 4.5)

    def test_delete_reservation(self):
        """Test deleting a Reservation instance"""
        reservation_id = self.reservation.id
        self.reservation.delete()
        with self.assertRaises(Reservations.DoesNotExist):
            Reservations.objects.get(id=reservation_id)

class AccommodationTestCase(TestCase):
    def setUp(self):
        """Create test data"""
        self.accommodation = Accommodation.objects.create(
            type="Single Room",
            period_of_availability="2023-06-01 to 2023-12-31",
            number_of_beds=1,
            number_of_bedrooms=1,
            room_id=101,
            price=100.00,
            distance=5.0
        )

    def test_create_accommodation(self):
        """Test creating an Accommodation instance"""
        self.assertEqual(self.accommodation.type, "Single Room")
        self.assertEqual(self.accommodation.room_id, 101)
        self.assertEqual(self.accommodation.price, 100.00)

    def test_update_accommodation(self):
        """测试 Accommodation 更新功能"""
        self.accommodation.price = 120.00
        self.accommodation.save()
        updated_accommodation = Accommodation.objects.get(id=self.accommodation.id)
        self.assertEqual(updated_accommodation.price, 120.00)

    def test_delete_accommodation(self):
        """Test deleting an Accommodation instance"""
        accommodation_id = self.accommodation.id
        self.accommodation.delete()
        with self.assertRaises(Accommodation.DoesNotExist):
            Accommodation.objects.get(id=accommodation_id)

class AdminTestCase(TestCase):
    def setUp(self):
        """Create test data"""
        self.admin = Admin.objects.create(
            username="admin1234",
            password="password123",
            email="admin@hku.com"
        )

    def test_create_admin(self):
        """测试 Admin 创建功能"""
        self.assertEqual(self.admin.username, "admin1234")
        self.assertEqual(self.admin.email, "admin@hku.com")
        self.assertTrue(self.admin.is_active)

    def test_admin_str(self):
        """Test creating an Admin instance"""
        self.assertEqual(str(self.admin), "admin1234")

    def test_update_admin(self):
        """Test updating an Admin instance"""
        self.admin.is_active = False
        self.admin.save()
        updated_admin = Admin.objects.get(id=self.admin.id)
        self.assertFalse(updated_admin.is_active)

    def test_delete_admin(self):
        """Test deleting an Admin instance"""
        admin_id = self.admin.id
        self.admin.delete()
        with self.assertRaises(Admin.DoesNotExist):
            Admin.objects.get(id=admin_id)