import React from "react";
import ProgressBar from "./ProgressBar";
import VerticalList from "./VerticalList";
import HorizontalList from "./HorizontalList";

const ProjectHeaderContent = ({
  Duration,
  TimeLeft,
  Description,
  Date,
  title,
  Progress,
  profile,
  banner,
}) => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        width: "100%",
        maxWidth: "60vw",
        marginTop: "-14.5%",
      }}
    >
      <div
        style={{
          position: "relative",
          zIndex: 1,
          flex: "1", // Take 1/3 of the available vertical space
        }}
      >
        <img
          src={banner}
          className="card-img-top"
          alt="Banner"
          style={{
            width: "100%",
            transform: "translateY(70%)",
          }}
        />
      </div>

      <div
        style={{
          background: "white",
          padding: "20px",
          borderRadius: "10px",
          flex: "2", // Take 2/3 of the available vertical space
        }}
      >
        <VerticalList
          spacing={10}
          items={[
            <img
              src={profile}
              alt="Profile"
              className="card-img-top"
              style={{
                width: "15%",
                height: "20%",
                borderRadius: "60%",
                objectFit: "cover",
                border: "3px solid white",
                position: "relative",
                zIndex: 2,
              }}
            />,
            <div
              style={{
                fontSize: "27px",
                fontWeight: "400",
              }}
            >
              {title}
            </div>,
            <HorizontalList
              spacing={20}
              items={[
                <div>{Duration}</div>,
                <div style={{ color: "#0A66C2",}}>
                  {TimeLeft}
                </div>,
              ]}
            />,
            <HorizontalList
              items={[
                <div>{Description}</div>,
                <div
                  style={{
                    marginLeft: "40px",
                    width: "200px",
                    transform: "translate(-10%,-15%)",
                  }}
                >
                  <ProgressBar
                    title={
                      <div style={{ fontSize: "18px", paddingBottom: "5px" }}>
                        <span style={{ fontWeight: "600" }}>Progress : </span>
                        {Progress}% complete
                      </div>
                    }
                    percentage={Progress}
                    date={Date}
                  />
                </div>,
              ]}
            />,
          ]}
        />
      </div>
    </div>
  );
};

export default ProjectHeaderContent;
