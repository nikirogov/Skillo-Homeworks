class Tenant:
    def __init__(self, name, contact, start_date):
        self.name = name
        self.contact = contact
        self.start_date = start_date

    def get_name(self):
        return self.name
    def get_contact(self):
        return self.contact
    def get_start_date(self):
        return self.start_date

    def update_concact_info(self, contact):
        self.contact = new_contact
        print("Contact info changed successfully")

class Tenant_info(Tenant):
    def __init__(self):
        self.tenants = []
    def add_tenant(self, tenant):
        tenant_id = len(self.tenants) + 1
        tenant.tenant_id = tenant_id
        self.tenants.append(tenant)
        print(f'Tenant {tenant.name} is added to the system with ID {tenant.tenant_id}')

    def find_tenant(self, tenant_id):
        for tenant in self.tenants:
            if tenant.tenant_id == tenant_id:
                return tenant
        return "Tenant not found"

    def update_lease_history(self, tenant_id, new_lease_history):
        tenant = self.find_tenant(tenant_id)
        if tenant:
            tenant.lease_history = new_lease_history
            print(f'Lease history: {new_lease_history} updated for Tenant with id: {tenant_id}')
        else:
            print(f'tenant ID {tenant_id} not found')



