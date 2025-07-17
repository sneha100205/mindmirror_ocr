BIAS_EXPLANATIONS = {
    "confirmation_bias": "You might be interpreting info to confirm what you already believe.",
    "negativity_bias": "You may be focusing too much on negative outcomes.",
    "anchoring_bias": "You could be relying heavily on initial information (first impressions)."
}

def explain_bias(bias_list):
    return [BIAS_EXPLANATIONS[bias] for bias in bias_list]
