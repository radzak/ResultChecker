import re


class HumanSorting:
    @staticmethod
    def atoi(text):
        return int(text) if text.isdigit() else text

    def key(self, text):
        """
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        """
        return [self.atoi(c) for c in re.split('(\d+)', text)]


def human_sorted(in_files_data):
    """
    :param in_files_data: List of 2-elem dicts containing in_file data 'name' and 'content'
    :return: sorted list_of_dicts by names of in_files
    """
    sort = HumanSorting()
    return sorted(in_files_data, key=lambda dikt: sort.key(dikt['name']))
