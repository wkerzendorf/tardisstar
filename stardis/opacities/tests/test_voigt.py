import pytest
from numpy import allclose, pi as PI
from math import sqrt
from stardis.opacities import voigt


@pytest.mark.parametrize(
    "faddeeva_input, faddeeva_expected_result",
    [
        (0, 1 + 0j),
        (0.0, 1.0 + 0.0j),
    ],
)
def test_faddeeva_sample_values(faddeeva_input, faddeeva_expected_result):
    assert allclose(voigt.faddeeva(faddeeva_input), faddeeva_expected_result)


@pytest.mark.parametrize(
    "voigt_input_delta_nu, voigt_input_doppler_width, voigt_input_gamma, voigt_expected_result",
    [
        (0, 1, 0, 1 / sqrt(PI)),
        (0, 2, 0, 1 / (sqrt(PI) * 2)),
    ],
)
def test_voigt_sample_values(
    voigt_input_delta_nu,
    voigt_input_doppler_width,
    voigt_input_gamma,
    voigt_expected_result,
):
    assert allclose(
        voigt.voigt_profile(
            voigt_input_delta_nu, voigt_input_doppler_width, voigt_input_gamma
        ),
        voigt_expected_result,
    )
