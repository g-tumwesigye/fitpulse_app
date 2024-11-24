import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "https://fitpulse-app.onrender.com";

  // Fetching predictions for the Body Fat Percentage based on user input
  static Future<double> predictBodyFat({
    required double weight,
    required double height,
    required double bmi,
    required String gender,
    required int age,
  }) async {
    final url = Uri.parse("$baseUrl/predict");

    // Sending data to the FastAPI backend for prediction
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "Weight": weight,
        "Height": height,
        "BMI": bmi,
        "Gender": gender,
        "Age": age,
      }),
    );

    // Handling response from the server
    if (response.statusCode == 200) {
      final Map<String, dynamic> responseData = jsonDecode(response.body);
      if (responseData.containsKey("Predicted Body Fat Percentage")) {
        return responseData["Predicted Body Fat Percentage"];
      } else {
        throw Exception("Invalid response format: Missing 'Predicted Body Fat Percentage'.");
      }
    } else {
      throw Exception("Failed to fetch prediction: ${response.body}");
    }
  }
}
