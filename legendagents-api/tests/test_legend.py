import pytest
from pydantic import ValidationError

from legendagents.legend import Legend, LegendFactory, LEGEND_NAMES
from legendagents.domain.exceptions import LegendNameNotFound


class TestLegendModel:
    def test_fields_are_stored(self, sample_legend):
        assert sample_legend.id == "einstein"
        assert sample_legend.name == "Albert Einstein"
        assert sample_legend.perspective
        assert sample_legend.style

    def test_str_contains_id_and_name(self, sample_legend):
        result = str(sample_legend)
        assert "einstein" in result
        assert "Albert Einstein" in result

    def test_missing_required_field_raises(self):
        with pytest.raises(ValidationError):
            Legend(name="Test", perspective="p", style="s")  # missing id


class TestLegendFactory:
    def test_returns_legend_instance(self):
        legend = LegendFactory.get_legend("einstein")
        assert isinstance(legend, Legend)

    def test_name_matches_registry(self):
        legend = LegendFactory.get_legend("gandhi")
        assert legend.name == "Mahatma Gandhi"

    def test_id_is_case_insensitive(self):
        legend = LegendFactory.get_legend("EINSTEIN")
        assert legend.name == "Albert Einstein"

    def test_unknown_id_raises_name_not_found(self):
        with pytest.raises(LegendNameNotFound):
            LegendFactory.get_legend("plato")

    def test_legend_has_non_empty_perspective_and_style(self):
        legend = LegendFactory.get_legend("newton")
        assert legend.perspective
        assert legend.style

    @pytest.mark.parametrize("legend_id", LEGEND_NAMES.keys())
    def test_all_defined_legends_are_loadable(self, legend_id):
        legend = LegendFactory.get_legend(legend_id)
        assert legend.name == LEGEND_NAMES[legend_id]
        assert legend.perspective
        assert legend.style
