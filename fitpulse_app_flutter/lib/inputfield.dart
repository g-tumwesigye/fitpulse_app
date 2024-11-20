import 'package:flutter/material.dart';
import 'api_service.dart';

class InputFieldPage extends StatefulWidget {
  @override
  _InputFieldPageState createState() => _InputFieldPageState();
}

class _InputFieldPageState extends State<InputFieldPage> {
  final TextEditingController _weightController = TextEditingController();
  final TextEditingController _heightController = TextEditingController();
  final TextEditingController _bmiController = TextEditingController();
  final TextEditingController _ageController = TextEditingController();
  final TextEditingController _genderController = TextEditingController();
  String? _result;

  void _getPrediction() async {
    try {
      final weight = double.parse(_weightController.text);
      final height = double.parse(_heightController.text);
      final bmi = double.parse(_bmiController.text);
      final age = int.parse(_ageController.text);
      final gender = _genderController.text;

      final response = await ApiService.predictBodyFat(
        weight: weight,
        height: height,
        bmi: bmi,
        gender: gender,
        age: age,
      );

      setState(() {
        _result = "Body Fat Percentage: ${response['Body Fat Percentage']}%";
      });
    } catch (e) {
      setState(() {
        _result = "Error: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Center(
              child: Text(
                'BODY FAT % PREDICTION',
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            SizedBox(height: 20),
            _buildTextField("Weight", _weightController),
            SizedBox(height: 16),
            _buildTextField("Height", _heightController),
            SizedBox(height: 16),
            _buildTextField("BMI", _bmiController),
            SizedBox(height: 16),
            _buildTextField("Age", _ageController),
            SizedBox(height: 16),
            _buildTextField("Gender (Male/Female)", _genderController),
            SizedBox(height: 40),
            Center(
              child: ElevatedButton(
                onPressed: _getPrediction,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xFFB26A2D),
                  padding: EdgeInsets.symmetric(horizontal: 80, vertical: 22),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                ),
                child: Text(
                  'Predict',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ),
            SizedBox(height: 20),
            if (_result != null)
              Center(
                child: Text(
                  _result!,
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  textAlign: TextAlign.center,
                ),
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildTextField(String label, TextEditingController controller) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label),
        SizedBox(height: 8),
        TextField(
          controller: controller,
          decoration: InputDecoration(
            filled: true,
            fillColor: Colors.grey.shade300,
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(5.0),
              borderSide: BorderSide.none,
            ),
          ),
        ),
      ],
    );
  }
}
