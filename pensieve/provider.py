class ModelProvider:
    provider_registry = dict()

    def __init_subclass__(cls, provider_keys=None, **kwargs):
        if provider_keys is None:
            raise TypeError(f'{cls.__name__} must include a provider key')

        super().__init_subclass__(**kwargs)

        for key in provider_keys:
            ModelProvider.provider_registry[key] = cls

    def __new__(cls, provider_key=None, **kwargs):
        subclass = cls.provider_registry.get(provider_key)

        if subclass is None:
            raise TypeError(f'No valid implementation for \"{provider_key}\" found')

        return super().__new__(subclass)

    def get_model(self, model_key: str):
        raise NotImplementedError()


