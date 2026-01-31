
import os

file_path = r'D:\DriveX\Owner\templates\Owner\edit_vehicle.html'

content = """{% extends 'DriveX/base.html' %}
{% load static %}

{% block content %}
<div class="profile-edit-section">
    <div class="container">
        <div class="profile-edit-card reveal">
            <div class="card-header">
                <h2>Edit Vehicle</h2>
                <p>Update your vehicle details below.</p>
            </div>
            
            <form method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                
                <div class="form-grid">
                    <div class="input-group-auth">
                        <label>Display Name</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-car"></i>
                            <input type="text" name="name" value="{{ form.name.value|default:'' }}" required>
                        </div>
                    </div>

                    <div class="input-group-auth">
                        <label>Brand</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-tag"></i>
                            <input type="text" name="brand" value="{{ form.brand.value|default:'' }}" required>
                        </div>
                    </div>

                    <div class="input-group-auth">
                        <label>Model</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-layer-group"></i>
                            <input type="text" name="model" value="{{ form.model.value|default:'' }}" required>
                        </div>
                    </div>

                    <div class="input-group-auth">
                        <label>Price per Day</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-dollar-sign"></i>
                            <input type="number" name="price_per_day" value="{{ form.price_per_day.value|default:'' }}" required>
                        </div>
                    </div>
                    
                    <div class="input-group-auth">
                        <label>License Plate</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-id-card"></i>
                            <input type="text" name="license_plate" value="{{ form.license_plate.value|default:'' }}" required>
                        </div>
                    </div>

                    <div class="input-group-auth">
                        <label>Fuel Type</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-gas-pump"></i>
                            <select name="fuel_type" class="custom-select">
                                {% for value, label in form.fields.fuel_type.choices %}
                                <option value="{{ value }}" {% if form.fuel_type.value == value %}selected{% endif %}>{{ label }}</option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
                </div>

                <div class="form-actions" style="margin-top: 2rem;">
                    <a href="{% url 'Owner:dashboard' %}" class="btn-secondary">Cancel</a>
                    <button type="submit" class="btn-primary">Save Changes</button>
                </div>
            </form>
        </div>
    </div>
</div>

<style>
    /* Reuse styles from edit_profile.html context */
    .profile-edit-section {
        padding: 4rem 1rem;
        min-height: 80vh;
        background: #f8fafc;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 60px;
    }

    .profile-edit-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        width: 100%;
        max-width: 800px;
        animation: slideUp 0.4s ease-out;
    }

    .card-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .card-header h2 {
        font-size: 1.8rem;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }

    .form-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }

    @media (max-width: 768px) {
        .form-grid {
            grid-template-columns: 1fr;
        }
    }

    .input-group-auth label {
        display: block;
        margin-bottom: 0.5rem;
        color: #475569;
        font-weight: 500;
        font-size: 0.9rem;
    }

    .input-wrapper {
        position: relative;
    }

    .input-wrapper i {
        position: absolute;
        left: 1rem;
        top: 50%;
        transform: translateY(-50%);
        color: #94a3b8;
    }

    .input-wrapper input, .input-wrapper select {
        width: 100%;
        padding: 0.8rem 1rem 0.8rem 2.8rem;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        font-size: 0.95rem;
        transition: all 0.2s;
        background: #f8fafc;
    }

    .input-wrapper input:focus {
        border-color: #3b82f6;
        background: white;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        outline: none;
    }

    .btn-primary, .btn-secondary {
        padding: 0.8rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;
        border: none;
        font-size: 1rem;
        transition: transform 0.1s;
    }

    .btn-primary {
        background: #2563eb;
        color: white;
        flex: 1;
    }

    .btn-secondary {
        background: #e2e8f0;
        color: #475569;
        margin-right: 1rem;
    }

    .form-actions {
        display: flex;
        justify-content: flex-end;
    }
</style>
{% endblock %}
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully overwrote {file_path}")
