import pytest

from aiden.decisions.laya import LayaDecisionProvider


@pytest.mark.asyncio
async def test_laya_decision():

    decision_provider = LayaDecisionProvider()

    result = await decision_provider.decide(
        question="Should the agent retrieve long-term memory?",
        context="The user asks about something they previously told the agent.",
    )

    print("\nLaya decision:", result)

    assert result
    assert result.type == "noul"
    assert 0.0 <= result.score <= 1.0
    assert 0.0 <= result.confidence <= 1.0
    assert 0.0 <= result.answer_confidence <= 1.0
    assert 0.0 <= result.act_probability <= 1.0
    assert result.is_positive is True