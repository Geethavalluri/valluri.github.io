from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data — replace with your own cleaned location list or load from file
locations = [
    "1st block jayanagar", "1st phase jp nagar", "whitefield", "btm layout",
    "electronic city", "rajaji nagar", "hebbal", "marathahalli",
    "banashankari", "bannerghatta road", "hsr layout","2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", 
    "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", 
    "9th phase jp nagar", "abbigere", "aecs layout", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", 
    "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "babusapalaya", "badavala nagar", "balagere", 
    "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", 
    "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", 
    "bellandur", "beml layout", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", 
    "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "btm 2nd stage", "btm layout", "budigere", "chamrajpet", 
    "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", "choodasandra", "cooke town", "cox town",
      "cunningham road", "cv raman nagar", "dasanapura", "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", 
      "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "electronic city", "electronic city phase ii", 
      "electronics city phase 1", "epip zone", "frazer town", "garudachar palya", "giri nagar", "gm palaya", "gollarapalya hosahalli", 
      "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "haralur road", "harlur", "hbr layout", "hebbal", 
      "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", 
      "hosakerehalli", "hoskote", "hosur road", "hrbr layout", "hsr layout", "hulimavu", "iblur village", "indira nagar", "isro layout", 
      "itpl", "jakkur", "jalahalli", "jalahalli east", "jigani", "jp nagar", "judicial layout", "kadubeesanahalli", "kadugodi", 
      "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", 
      "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", 
      "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", 
      "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kr puram", "kudlu", "kudlu gate", "kumaraswami layout",
        "kundalahalli", "laggere", "lakshminarayana pura", "lb shastri nagar", "lingadheeranahalli", "magadi road", "mahadevpura", 
        "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", 
        "munnekollal", "murugeshpalya", "mysore road", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura",
          "neeladri nagar", "nehru nagar", "ngr layout", "nri layout", "old airport road", "old madras road", "ombr layout", "other", 
          "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", 
          "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", 
          "rayasandra", "sahakara nagar", "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", 
          "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya",
            "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "talaghattapura", "tc palaya", "thanisandra", "thigalarapalya", 
            "thubarahalli", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", 
            "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", 
            "yelahanka new town", "yelenahalli", "yeshwanthpur"
]

# Dummy prediction function — replace this with your actual model logic
def estimate_price(sqft, bhk, bath, location):
    # Example: Rs 5000 per sqft base price, modifiers added
    base_price_per_sqft = 5000

    # Add modifiers
    bhk_bonus = (bhk - 1) * 0.05  # 5% extra per BHK
    bath_bonus = (bath - 1) * 0.03  # 3% extra per bathroom

    modifier = 1 + bhk_bonus + bath_bonus
    estimated_price = sqft * base_price_per_sqft * modifier

    # Convert to lakhs
    return round(estimated_price / 100000, 2)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({
        'locations': sorted(locations)
    })

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Log incoming data for debugging
        print("Form data:", request.form)

        # Safely parse form values
        total_sqft = request.form.get('total_sqft')
        bhk = request.form.get('bhk')
        bath = request.form.get('bath')
        location = request.form.get('location')

        # Validate
        if not (total_sqft and bhk and bath and location):
            return jsonify({'error': 'Missing input fields'}), 400

        # Convert to appropriate types
        total_sqft = float(total_sqft)
        bhk = int(bhk)
        bath = int(bath)

        if location not in locations:
            return jsonify({'error': f'Invalid location: {location}'}), 400

        estimated_price = estimate_price(total_sqft, bhk, bath, location)
        return jsonify({'estimated_price_lakhs': estimated_price})

    except Exception as e:
        return jsonify({
            'error': 'Something went wrong',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
