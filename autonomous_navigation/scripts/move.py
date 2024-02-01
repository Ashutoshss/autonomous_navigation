class Movement:
    def moveup(self):
        print("moving up")
    def movedown(self):
        print("moving down")

<?xml version="1.0"?>

<robot name="myfirst">

    <material name="grey">
        <color rgba="0.7 0.7 0.7 1"/>
    </material>
    
    <material name="green">
        <color rgba="0 0.6 0 1"/>
    </material>
    
    <material name="white">
        <color rgba="0 0 0 0"/>
    </material>

    <!-- <link name = "base_link">
        <visual>
            <geometry>
                <box size="0.6 0.4 0.2"/>
            </geometry>
            <orign xyz="0 0 0" rpy="0 0 0"/>
            <material name ="green"/>
        </visual>
    </link>

    <link name="lidar">
        <visual>
            <geometry>
                <cylinder length="0.05" radius="0.1"/>
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0"/>
            <material name="white"/>
        </visual>
    </link>

    <joint name="base_lidar_joint" type="fixed">
        <parent link="base_link"/>
        <child link="lidar"/>
        <origin xyz="0 0 0.125" rpy="0 0 0"/>
    </joint> -->
    
    <link
    name="base_link">
    <inertial>
      <origin
        xyz="0.04043 -0.066305 0.051189"
        rpy="0 0 0" />
      <mass
        value="0.2486" />
      <inertia
        ixx="0.00013491"
        ixy="2.978E-21"
        ixz="2.0711E-06"
        iyy="0.00020432"
        iyz="2.2788E-21"
        izz="0.0002708" />
    </inertial>
    <visual>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/base_link.STL" />
      </geometry>
      <material>
        <color name = "white"/>
      </material>
    </visual>
    <collision>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/base_link.STL" />
      </geometry>
    </collision>
  </link>

  <link
    name="Left_Wheel_Link">
    <inertial>
      <origin
        xyz="3.4694E-18 -0.005 0"
        rpy="0 0 0" />
      <mass
        value="0.007854" />
      <inertia
        ixx="8.9994E-07"
        ixy="1.0317E-22"
        ixz="-1.0037E-38"
        iyy="1.2763E-06"
        iyz="1.379E-39"
        izz="8.9994E-07" />
    </inertial>
    <visual>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/Left_Wheel_Link.STL" />
      </geometry>
      <material
        name="">
        <color
          rgba="0.79216 0.81961 0.93333 1" />
      </material>
    </visual>
    <collision>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/Left_Wheel_Link.STL" />
      </geometry>
    </collision>
  </link>

  <link
    name="Right_Wheel_Link">
    <inertial>
      <origin
        xyz="0.04043 -0.066305 0.051189"
        rpy="0 0 0" />
      <mass
        value="0.2486" />
      <inertia
        ixx="0.00013491"
        ixy="2.978E-21"
        ixz="2.0711E-06"
        iyy="0.00020432"
        iyz="2.2788E-21"
        izz="0.0002708" />
    </inertial>
    <visual>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/Right_Wheel_Link.STL" />
      </geometry>
      <material
        name="">
        <color
          rgba="0.79216 0.81961 0.93333 1" />
      </material>
    </visual>
    <collision>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://autonomous_navigation/meshes/Right_Wheel_Link.STL" />
      </geometry>
    </collision>
  </link>

  <joint
    name="leftjoint"
    type="continuous">
    <origin
      xyz="0 0.08 0"
      rpy="0 0 0" />
    <parent
      link="base_link" />
    <child
      link="Left_Wheel_Link" />
    <axis
      xyz="0 1 0" />
    <limit
      effort="1"
      velocity="1" />
  </joint>

  <joint
    name="rightjoint"
    type="continuous">
    <origin
      xyz="0 -0.001 0"
      rpy="0 0 0" />
    <parent
      link="base_link" />
    <child
      link="Right_Wheel_Link" />
    <axis
      xyz="0 1 0" />
    <limit
      effort="1"
      velocity="1" />
  </joint>

</robot>
