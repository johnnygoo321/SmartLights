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
  const [state, setState] = useState({ red: 255, green: 118, blue: 0 });

  const configureLedStrip = (endpoint) => {
    let baseUrl = IPV4_ADDRESS_OF_PI + ":" + SERVER_PORT + "/" + endpoint,
      data = { red: state.red, green: state.green, blue: state.blue };

    axios
      .post(baseUrl, data, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
      .then(
        (response) => {
          // Toast.show({
          //   type: "success",
          //   text1: "TEST",
          //   visibilityTime: 2000,
          // });
        },
        (error) => {
          // Toast.show({
          //   type: "error",
          //   text1: "Could not configure light settings.",
          //   text2:
          //     "Ensure your Pi is on and connected to the Smart Light Device.",
          //   visibilityTime: 2500,
          // });
          console.log(error);
        }
      );
  };

  const toastConfig = {
    success: ({ text1, text2, ...rest }) => (
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

    error: ({ text1, text2, ...rest }) => (
      <BaseToast
        {...rest}
        style={{ borderLeftColor: "#FF9900", backgroundColor: "#fff" }}
        contentContainerStyle={{ paddingHorizontal: 15 }}
        text1Style={{
          fontSize: width / 21,
        }}
        text2Style={{
          color: "#000",
          fontSize: width / 26,
        }}
        text1={text1}
        text2={text2}
      />
    ),
  };

  return (
    <View
      style={{
        alignItems: "center",
      }}
    >
      <Toast style={{ zIndex: 1 }} config={toastConfig} />
      <ColorPicker
        sliderComponent={Slider}
        hideSliders={true}
        defaultColor={"orange"}
        onColorSelected={() => configureLedStrip("noEffect")}
        onColorChange={(color) => setState(hexRgb(fromHsv(color)))}
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
  );
};

export default SmartLights;
