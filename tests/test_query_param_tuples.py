import pytest
import httpx

def test_query_param_sequence_of_tuples():
    """Verify QueryParams handles sequence of tuples with duplicate keys."""
    params = [("tag", "alpha"), ("tag", "beta"), ("sort", "desc")]
    qp = httpx.QueryParams(params)
    assert qp.get_list("tag") == ["alpha", "beta"]
    assert qp["sort"] == "desc"
    assert str(qp) == "tag=alpha&tag=beta&sort=desc"

def test_query_param_empty_values_preservation():
    """Verify empty query param values are preserved accurately in urlencode."""
    params = [("filter", ""), ("active", "true")]
    qp = httpx.QueryParams(params)
    assert str(qp) == "filter=&active=true"
    assert qp["filter"] == ""

def test_query_param_numeric_and_boolean_types():
    """Verify primitive values in dictionary query parameters format correctly."""
    params = {"count": 10, "enabled": True}
    qp = httpx.QueryParams(params)
    assert qp["count"] == "10"
    assert qp["enabled"] == "true"
