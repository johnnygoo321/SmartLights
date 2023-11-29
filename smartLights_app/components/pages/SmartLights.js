import React, { useState } from "react";
import { Dimensions, View } from "react-native";
import { ColorPicker, fromHsv } from "react-native-color-picker";
import { IPV4_ADDRESS_OF_PI, SERVER_PORT } from "@env";
import Toast, { BaseToast } from "react-native-toast-message";
import axios from "axios";
import Slider from "@react-native-community/slider";
import hexRgb from "hex-rgb";
import RoundedButton from "../buttons/RoundedButton";

const { width, height } = Dimensions.get("window");

const SmartLights = () => {
  const [rgbValue, setRgbValue] = useState({ red: 255, green: 118, blue: 0 });
  const [loading, setLoadingState] = useState(false);

  const configureLedStrip = async (endpoint) => {
    let baseUrl = IPV4_ADDRESS_OF_PI + ":" + SERVER_PORT + "/" + endpoint,
      data = { red: rgbValue.red, green: rgbValue.green, blue: rgbValue.blue };

    setLoadingState(true);
    Toast.show({
      type: "info",
      text1: "Processing Request",
      text2: "Please wait...",
      autoHide: false,
    });

    await axios
      .post(baseUrl, data, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
      .then(
        (response) => {
          console.log(response);
          setLoadingState(false);
          Toast.show({
            type: "success",
            text1: response.data,
            text2: "Animation Selected: " + endpoint,
            visibilityTime: 2500,
          });
        },
        (error) => {
          console.log("Miserable Failure Error: ", error);
          setLoadingState(false);
          Toast.show({
            type: "error",
            text1: "Could not configure LED Strip.",
            text2: "Check Error logs...",
            visibilityTime: 2500,
          });
        }
      );
  };

  const toastConfig = {
    success: ({ text1, text2, ...rest }) => (
      <BaseToast
        {...rest}
        style={{ borderLeftColor: "lightgreen", backgroundColor: "#fff" }}
        contentContainerStyle={{ paddingHorizontal: 15 }}
        text1Style={{
          fontSize: width / 22,
        }}
        text2Style={{
          color: "#000",
          fontSize: width / 25,
        }}
        text1={text1}
        text2={text2}
      />
    ),
    error: ({ text1, text2, ...rest }) => (
      <BaseToast
        {...rest}
        style={{ borderLeftColor: "red", backgroundColor: "#fff" }}
        contentContainerStyle={{ paddingHorizontal: 15 }}
        text1Style={{
          fontSize: width / 22,
        }}
        text2Style={{
          color: "#000",
          fontSize: width / 25,
        }}
        text1={text1}
        text2={text2}
      />
    ),
    info: ({ text1, text2, ...rest }) => (
      <BaseToast
        {...rest}
        style={{ borderLeftColor: "#FF9900", backgroundColor: "#fff" }}
        contentContainerStyle={{ paddingHorizontal: 15 }}
        text1Style={{
          fontSize: width / 22,
        }}
        text2Style={{
          color: "#000",
          fontSize: width / 25,
        }}
        text1={text1}
        text2={text2}
      />
    ),
  };

  return (
    <View pointerEvents={loading}>
      <View style={{ zIndex: 1 }}>
        <Toast config={toastConfig} />
      </View>
      <View
        style={{
          zIndex: 0,
          alignItems: "center",
        }}
      >
        <ColorPicker
          sliderComponent={Slider}
          hideSliders={true}
          defaultColor={"orange"}
          onColorSelected={() => configureLedStrip("noEffect")}
          onColorChange={(color) => setRgbValue(hexRgb(fromHsv(color)))}
          style={{ width: width, height: height / 2.3 }}
        />
        <RoundedButton
          onPress={() => configureLedStrip("wipe")}
          buttonText="Wipe"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("rainbow")}
          buttonText="Rainbow"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("rainbowCycle")}
          buttonText="Rainbow Cycle"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("theaterChase")}
          buttonText="Theater Chase"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("theaterChaseRainbow")}
          buttonText="Theater Chase Rainbow"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("randomize")}
          buttonText="Randomize"
        ></RoundedButton>
        <RoundedButton
          onPress={() => configureLedStrip("clear")}
          buttonText="Off"
        ></RoundedButton>
      </View>
    </View>
  );
};

export default SmartLights;
