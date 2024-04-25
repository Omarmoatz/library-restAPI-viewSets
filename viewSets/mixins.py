


class QuerySetMixin():
    # I made this mixin to not repeat the code
    user_field = 'user'

    def get_queryset(self ,*args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user 
        qs = super().get_queryset(*args, **kwargs)      
        return qs.filter(**lookup_data)  # self.user_field = self.request.user
    
  