def build_profile(first: str,
                  last: str,
                  **kwargs
                  ):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs


user_profile = build_profile(
    'albert',
    'einstein',
    location=False,
    field=True
)
print(user_profile)
