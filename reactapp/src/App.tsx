import "./App.css";
import { Header } from "./components/Header";
import { ListCard } from "./components/ListCard";
import ProjectMember from "./components/ProjectMember";
import ashesilogoblank from "./components/icons/ashesiblanklogo.png";
function App() {
  const descr =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus eros eu vehicula interdum. Cras nec ultricies massa. Curabitur rutrum, diam id consequat consequat";

  const TaskCon = (
    <ProjectMember
      Name={"Naruto Uzumaki"}
      role={"Research Assistant"}
      active={false}
      profile={ashesilogoblank}
    />
  );

  let content = [TaskCon, TaskCon, TaskCon];
  // content = [];
  return (
    <div className="app__body">
      <Header
        Page={
          <ListCard
            items={content}
            title={"Team Members"}
            NoItemMessage={"You have no team members"}
          />
        }
      />
    </div>
  );
}

export default App;
