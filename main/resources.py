from import_export import resources
from .models import Data_Profile
 
class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Data_Profile