# Logout button
        ttk.Button(self.root, text="Logout", command=self.logout).grid(row=7, column=0, columnspan=2, pady=10)

    def calculate_cost_and_time(self):
        start_point = self.selected_start_point.get()
        destination = self.destination_entry.get()

        route = self.find_route(start_point, destination)

        if route:
            cost_label = ttk.Label(self.root, text=f"Cost: ${route.cost:.2f}")
            cost_label.grid(row=8, column=0, columnspan=2, pady=5)

            distance_label = ttk.Label(self.root, text=f"Distance: {route.distance} km")
            distance_label.grid(row=9, column=0, columnspan=2, pady=5)

            estimated_time_label = ttk.Label(self.root, text=f"Estimated Time: {self.calculate_estimated_time(route.distance)} minutes")
            estimated_time_label.grid(row=10, column=0, columnspan=2, pady=5)
        else:
            ttk.Label(self.root, text="Route not found. Please check your input.").grid(row=8, column=0, columnspan=2, pady=5)

    def find_route(self, start_point, end_point):
        for route in self.routes:
            if route.start_point.name == start_point and route.end_point.name == end_point:
                return route
        return None

    def calculate_estimated_time(self, distance):
        # Assuming an average speed of 30 km/h for simplicity
        average_speed = 30
        time_in_hours = distance / average_speed
        time_in_minutes = time_in_hours * 60
        return int(time_in_minutes)

    def add_access_point(self, name, location):
        access_point = AccessPoint(name, location)
        self.access_points[name] = access_point

    def add_route(self, start_point, end_point, distance, vehicle_type, cost):
        route = Route(
            self.access_points[start_point],
            self.access_points[end_point],
            distance,
            vehicle_type,
            cost
        )
        self.routes.append(route)

    def logout(self):
        # Destroy the current window and recreate the login page
        self.root.destroy()
        root = tk.Tk()
        app = TransportationApp(root)
        root.mainloop()
