import React from "react";
import HorizontalList from "./HorizontalList";
import VerticalList from "./VerticalList";
import { Link } from "react-router-dom";

const AppsContent = ({ profile, title, descr }) => {
  return (
    <Link
      to="https://ashesi.instructure.com/login/canvas"
      style={{
        textDecoration: "none" /* Remove underline */,
        color: "inherit",
        fontWeight: "inherit",
      }}
    >
      <div>
        <HorizontalList
          spacing={10}
          items={[
            <img
              src={profile}
              alt=""
              style={{
                width: "50px",
                height: "50px",
                borderRadius: "20%",
                transform: "translateY(20px) ",
              }}
            />,
            <VerticalList
              spacing={10}
              items={[
                <div style={{ fontWeight: "500" }}>{title}</div>,
                <div
                  style={{
                    width: "60%",
                    fontSize: "12px", // Adjust the font size as needed
                    wordWrap: "break-word",
                  }}
                >
                  {descr}
                </div>,
              ]}
            />,
          ]}
        />
      </div>
    </Link>
  );
};

export default AppsContent;
