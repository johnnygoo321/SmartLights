import React from "react";
import { StyleSheet, Dimensions, Text, TouchableOpacity } from "react-native";

const { width, height } = Dimensions.get("screen");

export default RoundedButton = ({ onPress, buttonText }) => {
  return (
    <TouchableOpacity
      style={[styles.buttonStyle, { backgroundColor: "#1C1D2B" }]}
      onPress={onPress}
    >
      <Text style={styles.textStyle}>{buttonText}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  buttonStyle: {
    width: width / 1.2,
    height: height / 23,
    borderRadius: 30,
    borderColor: "#fff",
    borderWidth: 2,
    padding: 5,
    margin: 8,
  },
  textStyle: {
    textAlign: "center",
    fontSize: width / 25,
    paddingTop: 3,
    color: "#fff",
  },
});
