
class BaseSynthesizer:
    """Base class for all default synthesizers of ``SDGym``."""

    def fit(self, train_data):
        pass

    def sample(self, n):
        # TODO: Append data only
        pass

    def __init__(self, categoricals, ordinals, *args, **kwargs):
        self.categoricals = categoricals
        self.ordinals = ordinals
        # TODO: Remove working_dir
        # TODO: Use categoricals and ordinals

    @classmethod
    def run(cls, data, categoricals, ordinals):
        synthesizer = cls(categoricals, ordinals)
        synthesizer.fit(data)
        return synthesizer.sample(data.shape[0])
