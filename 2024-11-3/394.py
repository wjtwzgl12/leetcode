class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index):
            current_str = ""
            current_num = 0
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():  
                    current_num = current_num * 10 + int(char)
                elif char == '[': 
                    index, decoded_str = decode(index + 1)
                    current_str += decoded_str * current_num
                    current_num = 0
                elif char == ']': 
                    return index, current_str
                else:  
                    current_str += char
                
                index += 1
            
            return index, current_str
        
        _, result = decode(0)
        return result
