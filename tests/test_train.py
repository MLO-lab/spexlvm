from muvi import MuVI


def test_fit(data_gen):
    data_gen.generate()
    model = MuVI(
        data_gen.ys,
        data_gen.w_masks,
        data_gen.x,
        use_gpu=False,
    )
    model.fit(
        batch_size=0,
        n_epochs=10,
        n_particles=1,
        learning_rate=0.01,
        optimizer="clipped",
        verbose=0,
        seed=0,
    )

    assert model._trained
    assert model._cache is None
