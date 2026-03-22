"""Tests for validators."""

from istat_mcp_server.utils.validators import validate_dataflow_id, validate_keywords


def test_validate_keywords():
    """Test keyword validation."""
    # Empty string
    assert validate_keywords('') == []

    # Single keyword
    assert validate_keywords('population') == ['population']

    # Multiple keywords
    assert validate_keywords('population,employment,gdp') == ['population', 'employment', 'gdp']

    # With spaces
    assert validate_keywords(' population , employment ') == ['population', 'employment']

    # Case insensitive
    result = validate_keywords('Population,EMPLOYMENT')
    assert result == ['population', 'employment']


def test_validate_dataflow_id():
    """Test dataflow ID validation."""
    # Valid IDs
    assert validate_dataflow_id('101_1015_DF_DCSP_COLTIVAZIONI_1') is True
    assert validate_dataflow_id('SIMPLE_ID') is True
    assert validate_dataflow_id('ID123') is True

    # Invalid IDs
    assert validate_dataflow_id('') is False
    assert validate_dataflow_id('   ') is False
    assert validate_dataflow_id('id-with-dash') is False
    assert validate_dataflow_id('id with space') is False
    assert validate_dataflow_id('id@special') is False
