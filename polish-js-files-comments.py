import fileinput
import os
import pdb
import re
import sys

DOT_CHAR = "."
JSDOC_DOUBLE_SPACE_REGEXP = "^(^\s{1,}\*).+\s{2,}"
JSDOC_FULL_TITLE_REGEXP = "^\s{1,}\*\s{1,}(?:[a-zA-Z]{1,}\s{1,})+.{1,}"
JSDOC_NO_PARAM_REGEXP = "^\s{1,}\*.\@.[enum|retun].+\s{1,}\{.[a-zA-Z].+\}\s{1,}[a-zA-Z]"
JSDOC_PARAM_REGEX = "^\s{1,}\*.\@.[a-z].+\s{1,}\{"
JSDOC_PARAM_TEXT_REGEX = "^\s{1,}\*.\@.[param].+\s{1,}\{.[a-zA-Z].+\}\s{1,}[a-zA-Z]+\s{1,}"
JSDOC_TITLE_REGEXP = "^\s{1,}\*.[a-zA-Z]"
LIMIT_LINE_COL = 75
NULLABLE_CHAR = "!"
PARSER_CHAR = "{---}"
SPACE_LINE_CHAR = "\n"
NO_BREAK_SPACE_CHAR = " "


class PolishJSFileComments:
    def __init__(self, file_path):
        self.file_path = file_path
        self.list_fixes = []
        self.set_line_index = set()
        
    def _fix_jsdoc_capitalize(self, regexp):
        """
        Sets on list_fixes, letter capitalize on the jsdoc params.

        Args:
        String: regexp Pattern to match.
        """

        self.list_fixes = []
        nullable = ""
        line_fixed = ""
        for line in self.set_list_line_filtered(regexp):
            word_on_regex = re.findall(regexp, line[0])
            
            if word_on_regex:
                prefix_word = word_on_regex[0]
                suffix_word = re.split(regexp, line[0])[1]

                if suffix_word:    
                    suffix_letter_removed = suffix_word[1:]
                    first_letter_upper = suffix_word[0][0].upper()
                    if suffix_word[0] == NULLABLE_CHAR:
                        first_letter_upper = NULLABLE_CHAR + suffix_word[1][0].upper()
                        suffix_letter_removed = suffix_word[2:]

                    line_fixed = prefix_word + first_letter_upper + suffix_letter_removed
                    self.list_fixes.append((line[0], line_fixed))

                self.write_fixed_lines_on_file()

    def _fix_jsdoc_no_param_capitalize(self, regexp):
        """
        Sets on list_fixes, letter capitalize on no param jsdoc.
        Example: * @return {string} Id type web_gallery

        Args:
        String: regexp Pattern to match.
        """

        self.list_fixes = []
        line_fixed = ""
  
        for line in self.set_list_line_filtered(regexp):
            has_capital_to_set = True
            word_on_regex = re.findall(regexp, line[0])
            
            if word_on_regex:           
                for line_index in self.set_line_index:
                    if (line_index + 1) == line[1]:
                        has_capital_to_set = False   

                prefix_word = word_on_regex[0]
               
                if has_capital_to_set:
                    last_letter_prefix_upper = prefix_word[-1].upper()
                else:
                    last_letter_prefix_upper = prefix_word[-1]

                suffix_word = re.split(regexp, line[0])[1]
                prefix_last_letter_removed = prefix_word[:-1]
                line_fixed = prefix_last_letter_removed + last_letter_prefix_upper + suffix_word
                self.list_fixes.append((line[0], line_fixed))

            self.write_fixed_lines_on_file()

    def _fix_jsdoc_text_dot(self, regexp):
        """
        Sets on list_fixes, dot end on the jsdoc params text.

        Args:
        String: regexp Pattern to match.
        """
        
        self.list_fixes = []
        line_fixed = ""
        line_partial_fixed = ""
        regex = re.compile(r"[\n\r\t]")
        
        for line in self.set_list_line_filtered(regexp):
            word_on_regex = re.findall(regexp, line[0])
            prefix_word = word_on_regex[0]
            suffix_word = re.split(regexp, line[0])[1]
            last_suffix_letter = len(suffix_word) - 2

            if suffix_word:
                if DOT_CHAR != suffix_word[last_suffix_letter] and len(line[0]) < LIMIT_LINE_COL:
                    suffix_word = suffix_word + DOT_CHAR

                suffix_word = regex.sub("", suffix_word)
                line_partial_fixed = regex.sub("", line[0])
                line_fixed = prefix_word + suffix_word
                self.list_fixes.append((line_partial_fixed, line_fixed))

        self.write_fixed_lines_on_file()

    def _fix_jsdoc_title_text_dot(self, regexp):
        """
        Sets on list_fixes, dot end on the title jsdoc.

        Args:
        String: regexp Pattern to match.
        """
       
        self.list_fixes = []
        line_fixed_set = set()
        regex = re.compile(r"[\n\r\t]")
        line_fixed = ''

        for line in self.set_list_line_filtered(regexp):
            word_on_regex = re.findall(regexp, line[0])
            prefix_word = word_on_regex[0]
            last_prefix_letter = len(prefix_word) - 1

            if prefix_word:
                if DOT_CHAR != prefix_word[last_prefix_letter] and len(line[0]) < LIMIT_LINE_COL:
                    prefix_word = prefix_word + DOT_CHAR

                line_fixed = regex.sub("", line[0])
                line_fixed_set.add(line_fixed + PARSER_CHAR + prefix_word)
        
        for line in line_fixed_set:
            self.list_fixes.append((line.split(PARSER_CHAR)[0], line.split(PARSER_CHAR)[1]))
        self.write_fixed_lines_on_file()

    def _fix_double_space_on_jsdoc(self, regexp):
        """
        Sets on list_fixes, double spaces on jsdoc text.

        Args:
        String: regexp Pattern to match.
        """

        self.list_fixes = []
        line_fixed_set = set()
        line_fixed = ""
        line_filtered_inside = ""
        line_filtered_inside_prefix = ""

        for line in self.set_list_line_filtered(regexp):

            if line[0]:
                line_filtered_inside = re.split(r"^\s{1,}\*", line[0])[1]
                line_filtered_inside_prefix = re.search(r"^\s{1,}\*", line[0]).group()
                line_fixed = re.sub(r"\s{2,}", NO_BREAK_SPACE_CHAR, line_filtered_inside)
                line_fixed = line_filtered_inside_prefix + line_fixed
                line_fixed_set.add(line[0] + PARSER_CHAR + line_fixed)

            for line in line_fixed_set:
                self.list_fixes.append((line.split(PARSER_CHAR)[0], line.split(PARSER_CHAR)[1]))

        self.write_fixed_lines_on_file()

    def _matches(self, regexp, segment):
        """Matches segment with regexp provided.

        Args:
           String: regexp Pattern to match.
           String: segment To be macthed.

        Returns:
        Boolean True/False.
        """
        pattern_regexp = re.compile(regexp)

        return re.match(pattern_regexp, segment)

    def set_list_line_filtered(self, regexp):
        """
        Sets file lines list filtered with macth pattern in order to fix.

        Return:
        List file line filtered according regex.
        """

        list_line_filtered = []
        with open(self.file_path, 'r') as file:
            for index, line in enumerate(file):
                if (self._matches(regexp, line)):
                    list_line_filtered.append((line, index))
                    
                    if len(line) >= LIMIT_LINE_COL:
                        self.set_line_index.add(index)

        return list_line_filtered
    
    def write_fixed_lines_on_file(self):
        """Edits the file with the fixed lines.
        """
        current_file = open(self.file_path).read()
        list_fixes_length = len(self.list_fixes)
        for index, value in enumerate(self.list_fixes):
            current_file = current_file.replace(value[0], value[1])
            file_fixed = open(self.file_path, 'w')
            file_fixed.write(current_file)

            if index + 1 == list_fixes_length:
                file_fixed.close()

    def process(self):
        """
        Triggers fixes actions.
        """
        self._fix_double_space_on_jsdoc(JSDOC_DOUBLE_SPACE_REGEXP)
        self._fix_jsdoc_capitalize(JSDOC_PARAM_REGEX)
        self._fix_jsdoc_capitalize(JSDOC_PARAM_TEXT_REGEX)
        self._fix_jsdoc_no_param_capitalize(JSDOC_NO_PARAM_REGEXP)
        self._fix_jsdoc_no_param_capitalize(JSDOC_TITLE_REGEXP)
        
        
        
        
        
        
        self._fix_jsdoc_text_dot(JSDOC_NO_PARAM_REGEXP)
        
        
        
        
        
        
        self._fix_jsdoc_text_dot(JSDOC_PARAM_TEXT_REGEX)
        
        
        
        
        
        
        self._fix_jsdoc_title_text_dot(JSDOC_FULL_TITLE_REGEXP)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        PolishJSFileComments(arg).process()