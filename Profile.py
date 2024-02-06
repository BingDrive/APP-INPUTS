# Dropdown menu for selecting start point
        ttk.Label(self.root, text="Select Start Point:").grid(row=2, column=0, sticky=tk.W, pady=5)
        start_point_menu = ttk.Combobox(self.root, textvariable=self.selected_start_point)
        start_point_menu['values'] = list(self.access_points.keys())
        start_point_menu.grid(row=2, column=1, pady=5)
        start_point_menu.set("ICT")

        # Input form for entering destination
        ttk.Label(self.root, text="Enter Destination (End Point):").grid(row=3, column=0, sticky=tk.W, pady=5)
        destination_entry = ttk.Entry(self.root, textvariable=self.destination_entry)
        destination_entry.grid(row=3, column=1, pady=5)

        ttk.Button(self.root, text="Calculate Cost and Time", command=self.calculate_cost_and_time).grid(row=4, column=0, columnspan=2, pady=10)

        # Profile section
        ttk.Label(self.root, text="User Profile", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Label(self.root, text=str(self.current_user)).grid(row=6, column=0, columnspan=2, pady=5)
