from Tenants import Tenant
from Tenants import Tenant_info
from Rent_class import Rent
from  Apartment import Apartment

person1 = Tenant (
    name = 'Alice',
    contact = '123',
    start_date = '10/11/2022'
)

person2 = Tenant (
    name = 'Bob',
    contact = '1534',
    start_date = '14/06/2022'
)

rent1 = Rent(1000, "10/11/2023")
rent1 = Rent(1000, "14/06/2023")

apartment1 = Apartment("A101", 800, 1200)
apartment2 = Apartment("B202", 1000, 950)

tenant_info = Tenant_info()
tenant_info.add_tenant(person1)
tenant_info.add_tenant(person2)

tenant = tenant_info.find_tenant("Alice")
Tenant.get_name(person1)
Tenant.get_contact(person1)
Tenant.get_start_date(person1)
tenant.update_contact_info("new-email@example.com")

apartment1.display_details()