
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        try:
            if friend_name is None or not isinstance(friend_name, str):
                raise NotImplementedError()
            else:
                return f"Hello, {friend_name}"
        except Exception as e:
            return f"Error: {str(e)}"
