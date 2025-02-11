

import re

all_indicator_res = []
all_indicator_res_swda = []

# slightly modified regular expression from Noble et al's (2021) work
# https://www.semdial.org/anthology/Z21-Noble_semdial_0016.pdf
indicator_re = r"""
    (                               # indicator phrase
    (?:wtf|wat|how|what)\s          # question word (allow "how do you mean by") 
    (?:\w+\s){0,2}                  # 0-2 words (allow "what specifically do you mean by", "what is it you mean by")
    (?:do\s)?                       # optional "do" (allow "depends what you mean by")
    you\s                           # "you"
    (?:\w+\s){0,2}                  # 0-2 words (allow "what do you actually mean by"
    mean                            # "mean"
    )\s                             # end indicator phrase      
    (?:
      by\s                          # "by"
      (?:(?:an|a|the)\s)?           # optional determiner
      (?:\"(.+)\"|\'(.+)\'|(\w+))   # optional quotes around trigger
    |                               # OR
      (?:by\s)?                     # optional "by" 
      (?:(?:an|a|the)\s)?           # optional determiner
      (?:\"(.+)\"|\'(.+)\')         # quotes around trigger
     |                               # OR (added)
      (?:by\s)?                     # optional "by" 
      (?:(?:an|a|the)\s)?           # optional determiner
      (?:\"\"(.+)\"\"|\'\'(.+)\'\')         # OPTIONAL DOUBLE quotes around trigger  
    )
    """
# stopped excluding: (?!by\s(?:that|this))           # "what do you mean by this/that"
indicator_re = re.compile(indicator_re, re.IGNORECASE | re.VERBOSE)
all_indicator_res.append((indicator_re, "what do you mean by"))
all_indicator_res_swda.append((indicator_re, "what do you mean by"))


########## What 's/is/are ...?
### SWDA VERSION: "?" is not compulsory
indicator_re = r"what(\s?)(is|\'s|are) (?!(?:you|he|she|it|we|they|my|your|his|her|its|our|their|some|happening|going on|the best|the most|wrong|there)\b)(\"|\')?(\"|\')?\b\w+(?:\s+\w+){0,4}\b(\"|\')?(\"|\')?\s?\??"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "what is"))

#### NON-SWDA VERSION
indicator_re = r"what(\s?)(is|\'s|are) (?!(?:you|he|she|it|we|they|my|your|his|her|its|our|their|some|happening|going on|the best|the most|wrong|there)\b)(\"|\')?(\"|\')?\b\w+(?:\s+\w+){0,4}\b(\"|\')?(\"|\')?\s?\?+"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "what is"))

########## Is this/that what you mean
indicator_re = r"is (this|that) what you mean"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is this what you mean"))
all_indicator_res_swda.append((indicator_re, "is this what you mean"))

########## That would mean ... ?
indicator_re = r"(this|that) would mean"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "that would mean"))
all_indicator_res_swda.append((indicator_re, "that would mean"))

########## how do you mean that?
# SWDA VERSION
indicator_re = r"how do you mean that(\s?)?"
indicator_re = re.compile(indicator_re, re.IGNORECASE) # | re.VERBOSE)
all_indicator_res_swda.append((indicator_re, "how do you mean that"))
# NON-SWDA VERSION
indicator_re = r"how do you mean that(\s?)?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE) # | re.VERBOSE)
all_indicator_res.append((indicator_re, "how do you mean that"))

########## What sort of... ?
indicator_re = r"(what|which) (sort|kind) of (?!.*\b(?:have|do|did|can|would|will|has|does)\b)\b\w+(?:\s+\w+){0,4}\b\s?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "what sort/kind of"))
all_indicator_res_swda.append((indicator_re, "what sort/kind of"))

########## you mean
indicator_re = r"(?<!I know what )(?<!I see what )(?<!I get what )(?<!I understand what )you mean"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "you mean"))
all_indicator_res_swda.append((indicator_re, "you mean"))

########## Are you (maybe) talking about ... ? / You are talking about ... ?
# accept potential adverbs ("maybe" are you maybe talking...)
# SWDA VERSION
indicator_re = r"(are you|you are) (?:\w+\s){0,2}talking about .+?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "are you talking about"))
# NON-SWDA VERSION
indicator_re = r"(are you|you are) (?:\w+\s){0,2}talking about .+?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "are you talking about"))

########## in what/which way/sense .... ?
indicator_re = r"in (what|which) (way|sense)(.*?)"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "in what way/sense"))
all_indicator_res_swda.append((indicator_re, "in what way/sense"))

########## is that a/the...?
indicator_re = r"is that (really )?(a|the)?(\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')?.*?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is that a/the"))
all_indicator_res_swda.append((indicator_re, "is that a/the"))

########## is that what that/this is
# SWDA VERSION
indicator_re = r"is that what (this|that|these|those) (is|are).*?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "is that what that/this is"))
# NON-SWDA VERSION
indicator_re = r"is that what (this|that|these|those) (is|are).*?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is that what that/this is"))

########## is that what X is  (limited to 5 words)
# SWDA VERSION
indicator_re = r"is that what (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')? (is|are).*?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "is that what X is"))
# NON-SWDA VERSION
indicator_re = r"is that what (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')? (is|are).*?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is that what X is"))

########## What does X mean? (limited to 5 words)
indicator_re = r"what does (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')? mean(\s?)?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "what does X mean"))
all_indicator_res_swda.append((indicator_re, "what does X mean"))

########## What is/would be the difference between X and Y?
indicator_re = r"what ('s|is|would be) the (\b\w+\b[\s\r\n]*){0,5}difference"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "what is the difference between"))
all_indicator_res_swda.append((indicator_re, "what is the difference between"))

######### do you know what X is? (do you happen to / by any chance know...)
indicator_re = r"(do )?you (\b\w+\b[\s\r\n]*){0,5}know what (.*?) (is|are)\s?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "do you know what X is"))
all_indicator_res_swda.append((indicator_re, "do you know what X is"))

######### have you (ever) heard of...
indicator_re = r"have you (\b\w+\b[\s\r\n]*){0,5}heard of (.*?)\s?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "have you heard of"))
all_indicator_res_swda.append((indicator_re, "have you heard of"))

####### (can you) define
# avoiding expressions like "predefined" and "clearly-defined"
indicator_re = r"(can you )?\bdefine"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "can you define"))
all_indicator_res_swda.append((indicator_re, "can you define"))

########## Is X like Y?
indicator_re = "(is|are) (?!.*you|there|he|she|we)(\"|\')?(\b(\w+)\b[\s\r\n,]*){1,5}(\"|\')?(not)? (like|the same as)(.*?)\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is X like/the same as Y"))
all_indicator_res_swda.append((indicator_re, "is X like/the same as Y"))

########## this is not X
indicator_re = r"(this|that)(\s?)(is|\'s) not (\"|\')?((\w+)\b[\s\r\n,]*){1,5}(\"|\')?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "this is not X"))
all_indicator_res_swda.append((indicator_re, "this is not X"))
# For the next iteration, consider removing expressions like "that's not to say" or "that's not true"

########## this isn't X
# adds plural and contracted negation to the one above
indicator_re = r"(this|that|these|those)(\s?)(((isn|aren)(\s?)\'t)|((is|are)(\s?)n\'t)) (\"|\')?((\w+)\b[\s\r\n,]*){1,5}(\"|\')?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "this isn't X"))
all_indicator_res_swda.append((indicator_re, "this isn't X"))

########## is this not...?
# SWDA VERSION
indicator_re = r"is (this|that) not (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "is this not...?"))
# NON-SWDA VERSION
indicator_re = r"is (this|that) not (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "is this not...?"))

########## isn't this....?
# SWDA VERSION
indicator_re = r"(((isn|aren)(\s?)\'t)|((is|are)(\s?)n\'t)) (this|that|these|those) (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')?\?*"
# indicator_re = re.compile(indicator_re, re.IGNORECASE) ### 11/02/2025 used to be commented
# all_indicator_res_swda.append((indicator_re, "is this not...?")) ### 11/02/2025 used to be commented
# NON-SWDA VERSION
indicator_re = r"(((isn|aren)(\s?)\'t)|((is|are)(\s?)n\'t)) (this|that|these|those) (\"|\')?(?:\b\w+\b[\s\r\n,]*){1,5}(\"|\')?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "isn't this...?"))

########## are we talking...?
indicator_re = r"are we talking .*?\?"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "are we talking"))
all_indicator_res_swda.append((indicator_re, "are we talking"))

########## Can you explain the difference
indicator_re = r"(can|could) you (explain|clarify) the difference"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "can you explain the difference"))
all_indicator_res_swda.append((indicator_re, "can you explain the difference"))

##########The term
# not allowing their plural and avoid "spread the word", "the word of god", "terminology"
indicator_re = r"(?<!spread )(the|this) (word|term)(?!.*s|inology| of god)"
indicator_re = re.compile(indicator_re, re.IGNORECASE) # | re.VERBOSE)
all_indicator_res.append((indicator_re, "the term"))
all_indicator_res_swda.append((indicator_re, "the term"))

########## does X count as ?
# SWDA VERSION: No "?"
indicator_re = r"(does|do) (?:\b\w+\b[\s\r\n,]*){1,5} count as (?:\b\w+\b[\s\r\n,]*){1,5}\??"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res_swda.append((indicator_re, "does X count as Y"))
# NON-SWDA VERSION
indicator_re = r"(does|do) (?:\b\w+\b[\s\r\n,]*){1,5} count as (?:\b\w+\b[\s\r\n,]*){1,5}\??"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "does X count as Y"))

########## elaborate
indicator_re = r"((can|could|would) you)? (?:\b\w+\b[\s\r\n,]*){1,3} elaborate\??"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "elaborate"))
all_indicator_res_swda.append((indicator_re, "elaborate"))

##################### REGEXS BASED ON JENNY'S BNC SEARCHES

########## what X means
indicator_re = r"what (?:\b\w+\b[\s\r\n,]*){1,5} means"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "what X means"))
all_indicator_res_swda.append((indicator_re, "what X means"))

########## the meaning of
indicator_re = r"the meaning of"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "the meaning of"))
all_indicator_res_swda.append((indicator_re, "the meaning of"))

########## definition of
indicator_re = r"definition of"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "definition of"))
all_indicator_res_swda.append((indicator_re, "definition of"))
# Comment: later on we might want to have simply "definition"

########## word X means
indicator_re = r"word (?:\b\w+\b[\s\r\n,]*){1,5} means"
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "word X means"))
all_indicator_res_swda.append((indicator_re, "word X means"))

########## depends on what you mean
indicator_re = r"depends on what you mean "
indicator_re = re.compile(indicator_re, re.IGNORECASE)
all_indicator_res.append((indicator_re, "depends on what you mean"))
all_indicator_res_swda.append((indicator_re, "depends on what you mean"))
