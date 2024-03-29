import "bootstrap/dist/css/bootstrap.min.css";
import ashesilogoblank from "./components/icons/ashesiblanklogo.png";
import VerticalList from "./components/VerticalList";
import SubListCard from "./components/SubListCard";
import sidebanner from "./components/icons/sidebanner.png";
import { TeamEnrollment } from "./components/TeamEnrollment";
import Notification from "./components/Notification";

const Test = () => {
  const notificationElement = (
    <Notification
      title={"Onedrive Library"}
      text={
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat"
      }
      date={"11:23 - Aug 2023"}
    />
  );

  const notificationcontent = [
    notificationElement,
    notificationElement,
    notificationElement,
  ];

  const enrollmentrequests = (
    <TeamEnrollment
      Name={"Naruto Uzumaki"}
      Role={"Research Assistant"}
      // active={false}
      Profile={ashesilogoblank}
    />
  );

  const enrollmentlist = [
    enrollmentrequests,
    enrollmentrequests,
    enrollmentrequests,
  ];

  return (
    <div style={{ width: "60vw" }}>
      <VerticalList
        spacing={20}
        items={[
          <img
            className="card"
            src={sidebanner}
            alt=""
            style={{
              width: "25vw",
              paddingLeft: "20px",
              paddingRight: "20px",
              backgroundColor: "white",
              borderRadius: "10px",
              margin:"0px"
            }}
          />,
          <SubListCard
            items={notificationcontent}
            title={"Notifications (3)"}
            NoItemMessage={"You have no notifications"}
          />,
          <SubListCard
            items={enrollmentlist}
            title={"Team Enrollment Requests"}
            NoItemMessage={"No enrollment requests placed"}
          />,
        ]}
      />
      ,
    </div>
  );
};

export default Test;
