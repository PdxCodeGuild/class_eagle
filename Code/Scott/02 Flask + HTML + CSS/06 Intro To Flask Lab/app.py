from flask import Flask, render_template, request

def genPass(uppers, lowers, nums, specials):
    output = ''
    pass_word = ''

    while uppers > 0 or lowers > 0 or nums > 0 or specials > 0: #Keep going until the 'quota' for each type of character is filled
        rand_chr_val = rand.randint(ord('!'), ord('~')) # generate a random integer in range of [33, 126] on ASCII table
        
        if rand_chr_val <= ord('Z') and rand_chr_val >= ord('A'):  # if that int is in the range of the ASCII values of ['A','Z'], then it's uppercase type
            if uppers > 0: # double checked we haven't hit our max
                uppers -= 1 # if we haven't hit our max, subtract one from the 'quota'
                output += chr(rand_chr_val) # And convert it from int to the corresponding unicode char, ALSO, add it onto the output of what we already have
        elif rand_chr_val <= ord('z') and rand_chr_val >= ord('a'): # if that int is in the range of the ASCII values of ['a,'z'], then it's lowercase type
            if lowers > 0:
                lowers -= 1
                output += chr(rand_chr_val)
        elif rand_chr_val <= ord('9') and rand_chr_val >= ord('0'):  # if that int is in the range of the ASCII values of ['0','9'], then it's numerical type
            if nums > 0:
                nums -= 1
                output += chr(rand_chr_val)
        else:  # All other cases (for the given range [33, 126]), it's a special character
            if specials > 0:
                specials -= 1
                output += chr(rand_chr_val)


        # Debug statement!

        # print(f'''
        #     ============================
        #     Generated: {rand_chr_val} Corresponds to: {chr(rand_chr_val)}
        #     Uppercase left: {upper_count}
        #     Lowercase left: {lower_count}
        #     Numerical left: {num_count}
        #     Special C left: {special_count}
        #     ----------------------------
        #     Password so far: {output}
        #     ============================
        #         ''')

    pass_word = list(output) # Turn output into a list
    rand.shuffle(pass_word) # take list and shuffle it 
    pass_word = ''.join(pass_word) # rejoin into one string
    return pass_word

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        response = dict(request.form)
        print(dict(request.form))
        print(response['uppers'])
    return render_template('index.html')
    
app.run(debug=True)