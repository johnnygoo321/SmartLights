import { BaseToast } from "react-native-toast-message";
import { StyleSheet, Dimensions } from "react-native";

const { width } = Dimensions.get("window");

export default ToastConfig = {
  success: ({ text1, text2, ...rest }) => (
    <BaseToast
      {...rest}
      style={{ borderLeftColor: "lightgreen" }}
      contentContainerStyle={styles.toastContainer}
      text1Style={styles.text1Style}
      text2Style={styles.text2Style}
      text1={text1}
      text2={text2}
    />
  ),
  error: ({ text1, text2, ...rest }) => (
    <BaseToast
      {...rest}
      style={{ borderLeftColor: "red" }}
      contentContainerStyle={styles.toastContainer}
      text1Style={styles.text1Style}
      text2Style={styles.text2Style}
      text1={text1}
      text2={text2}
    />
  ),
  info: ({ text1, text2, ...rest }) => (
    <BaseToast
      {...rest}
      style={{ borderLeftColor: "#FF9900" }}
      contentContainerStyle={styles.toastContainer}
      text1Style={styles.text1Style}
      text2Style={styles.text2Style}
      text1={text1}
      text2={text2}
    />
  ),
};

const styles = StyleSheet.create({
  text1Style: {
    fontSize: width / 22,
  },
  text2Style: {
    color: "#000",
    fontSize: width / 25,
  },
  toastContainer: {
    paddingHorizontal: 15,
  },
});
