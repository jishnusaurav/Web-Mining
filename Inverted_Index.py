import re

class Appearance:
    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency        
    def __repr__(self):
        return str(self.__dict__)
class Database:
    def __init__(self):
        self.db = dict()
    def __repr__(self):
        return str(self.__dict__)    
    def get(self, id):
        return self.db.get(id, None)    
    def add(self, document):
        return self.db.update({document['id']: document})
    def remove(self, document):

        return self.db.pop(document['id'], None)

class InvertedIndex:
    """
    Inverted Index class.
    """
    def __init__(self, db):
        self.index = dict()
        self.db = db
    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)        
    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """
        
        # Remove punctuation from the text.
        clean_text = re.sub(r'[^\w\s]','', document['text'])
        terms = clean_text.split(' ')
        appearances_dict = dict()        # Dictionary with each term and the frequency it appears in the text.
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)
            
        # Update the inverted index
        update_dict = { key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items() }        
        self.index.update(update_dict)        # Add the document into the database
        self.db.add(document)        
        return document    
    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return { term: self.index[term] for term in query.split(' ') if term in self.index }

def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def main():
    db = Database()
    index = InvertedIndex(db)    
    document1 = {
        'id': '1',
        'text': 'ting, which eventually results in higher trade volumes. Government agencies are using this technology to classify threats and fight against terrorism. The predicting capability of mining applications can benefit society by '
    }    
    document2 = {
        'id': '2',
        'text': 'Web usage mining by itself does not create issues, but this technology when used on data of personal nature might cause concerns. The most criticized ethical issue involving web usage mining is the invasion of privacy. Privacy is considered lost when information concerning an individual is obtained.'
    }  
    document3 = {
        'id': '3',
        'text': ' Web usage mining by itself does not create issues, but this technology when used on data of personal nature might cause concerns. The most criticized ethical issue involving web usage mining is the invasion of privacy. Privacy is considered lost when information concerning an individual is obtained, used, or disseminated, especially if this occurs without the individua'
    }
    document4 = {
        'id': '4',
        'text': 'Web usage mining essentially has many advantages which makes this technology attractive to corporations including government agencies. This technology has enabled e-commerce to do personalized marketing, which eventually results in higher trade volumes. Government agencies are using this technology to classify threats and fight against terrorism. The predicting capability of mining applications can benefit society by identifying criminal activities. Companies can establish better customer relationship by understanding the needs of the customer better and reacting to customer needs faster. Companies can find, attract and retain customers; they can save on production costs by utilizing the acquired insight of customer requirements. They can increase profitability by target pricing based on the profiles created. They can even find customers who might default to a competitor the company will try to retai'
    }    
    document5 = {
        'id': '5',
        'text': 'tudies related to work[2] are concerned with two areas: constraint-based data mining algorithms applied in Web usage mining and developed software tools (systems). Costa and Seco demonstrated that web log mining can be used to extract semantic information (hyponymy relationships in particular) about the user and a given community'
    }  
    document6 = {
        'id': '6',
        'text': ' Web usage mining essentially has many advantages which makes this technology attractive to corporations including government agencies. This technology has enabled e-commerce to do personalized marketing, which eventually results in higher trade volumes. Government agencies are using this technology to classify threats and fight against terrorism. The predicting capability of mining applications can benefit society by identifying criminal activities. Companies can establish better customer relationship by understanding the needs of the customer better and reacting to customer needs faster. Companies can find, attract and retain customers; they can save on production costs by utilizing the acquired insight of customer requirements. They can increase profitability by target pricing based on the profiles created. They can even find customers who might default to a competitor the company will try to retai'
    }
    document7 = {
        'id': '7',
        'text': 'tudies related to work[2] are concerned with two areas: constraint-based data mining algorithms applied in Web usage mining and developed software tools (systems). Costa and Seco demonstrated that web log mining can be used to extract semantic information (hyponymy relationships in particular) about the user and a given community'
    }    
    document8 = {
        'id': '8',
        'text': 'Web structure mining can also have another direction – discovering the structure of Web document itself. This type of structure mining can be used to reveal the structure (schema) of Web pages, this would be good for navigation purpose and make it possible to compare/integrate Web page schemes. This type of structure mining will facilitate introducing database techniques for accessing information in Web pages by providing a reference schema.'

    }  
    document9 = {
        'id': '9',
        'text': ' Web structure mining can also have another direction – discovering the structure of Web document itself. This type of structure mining can be used to reveal the structure (schema) of Web pages, this would be good for navigation purpose and make it possible to compare/integrate Web page schemes. This type of structure mining will facilitate introducing database techniques for accessing information in Web pages by providing a reference schema.'

    }
    document10 = {
        'id': '10',
        'text': 'Web mining is the application of data mining techniques to discover patterns from the World Wide Web. As the name proposes, this is information gathered by mining the web. It makes utilization of automated apparatuses to reveal and extricate data from servers and web2 reports, and it permits organizations to get to both organized and unstructured information from browser activities, server logs, website and link structure, page content and different sources.'

    }
    index.index_document(document1)
    index.index_document(document2)
    index.index_document(document3)
    index.index_document(document4)
    index.index_document(document5)
    index.index_document(document6)
    index.index_document(document7)
    index.index_document(document8)
    index.index_document(document9)
    index.index_document(document10)
    search_term = input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)    
    for term in result.keys():
        for appearance in result[term]:
            # Belgium: { docId: 1, frequency: 1}
            document = db.get(appearance.docId)
        print(result[term])
        print("-----------------------------")    
 main()
