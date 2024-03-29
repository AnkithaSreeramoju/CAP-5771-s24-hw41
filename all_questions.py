# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "A person could be a Home Owner and have a Low Annual Income"    
    answers["(b) explain"] = "There are attribute combinations not explicitly covered by these rules, like a person with High Annual Income and Currently Employed" 
    answers["(c) explain"] = "A person is a Home Owner and Single, the rule applied first could determine the outcome."
    answers["(d) explain"] = "A default class ensures that every instance can be classified even if it does not meet any specific rule's conditions."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "Yes"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "An animal cannot simultaneously be an Aerial Creature, Aquatic Creature, warm-blooded, and fit the conditions of R4."
    answers["(b) example"] = "They cover all possible combinations of the given attributes"
    answers["(c) example"] = "Each rule applies to a distinct set of attributes, so the order in which they are applied does not affect the outcome."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "False"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm computes the gradient of the loss function with respect to each weight by propagating the error backwards through the network"
    answers["(b) explain"] = "The activations at each layer are computed based on the activations of the previous layer and the current layer’s weights, making it possible to compute activations in a feedforward manner from input to output."
    answers["(c) explain"] = "The vanishing gradient problem refers to the issue where gradients become increasingly smaller as the error is propagated back through the layers, leading to minimal changes in weights and thus slowing down or halting training"
    answers["(d) explain"] = "Gradients of loss with respect to weights at all layers are 0, as small adjustments could still potentially reduce the loss further, especially if regularization is applied."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = None
    answers["(a) P(X_2=1)"] = None
    answers["(a) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = None

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = None

    # float
    answers["(c) P(X_1=1 | +)"] = None
    answers["(c) P(X_1=1 | -)"] = None
    answers["(c) P(X_2=1 | +)"] = None
    answers["(c) P(X_2=1 | -)"] = None
    answers["(c) P(X_3=1 | +)"] = None
    answers["(c) P(X_3=1 | -)"] = None

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = None
    answers["(d) Row 2"] = None
    answers["(d) Row 3"] = None
    answers["(d) Row 4"] = None

    # float between 0 and 1
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = None
    answers["(b) K"] = None

    # explain_string
    answers["(a) explain"] = None
    answers["(b) explain"] = None

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None 
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
