"""Tests for Pydantic input models."""

from istat_mcp_server.api.models import GetDataInput


def test_get_data_input_accepts_primary_fields():
    """get_data accepts canonical field names."""
    params = GetDataInput.model_validate(
        {
            'id_dataflow': '22_315_DF_DCIS_POPORESBIL1_2',
            'dimension_filters': {'SEX': ['T']},
            'start_period': '2024',
            'end_period': '2025',
        }
    )

    assert params.id_dataflow == '22_315_DF_DCIS_POPORESBIL1_2'
    assert params.dimension_filters == {'SEX': ['T']}


def test_get_data_input_accepts_compat_aliases():
    """get_data accepts compatibility aliases used by some clients."""
    params = GetDataInput.model_validate(
        {
            'dataflow_id': '22_315_DF_DCIS_POPORESBIL1_2',
            'filters': {'SEX': ['T']},
            'start_period': '2024',
            'end_period': '2025',
        }
    )

    assert params.id_dataflow == '22_315_DF_DCIS_POPORESBIL1_2'
    assert params.dimension_filters == {'SEX': ['T']}
