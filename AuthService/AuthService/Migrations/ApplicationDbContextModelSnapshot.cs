﻿// <auto-generated />
using AuthService.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace AuthService.Migrations
{
    [DbContext(typeof(ApplicationDbContext))]
    partial class ApplicationDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "8.0.6")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("AuthService.Entities.Stock", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("Id"));

                    b.Property<string>("DateOfPrediction")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<int>("DaysPredicted")
                        .HasColumnType("integer");

                    b.Property<double>("PredictedReturn")
                        .HasColumnType("double precision");

                    b.Property<string>("Ticker")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Stocks");

                    b.HasData(
                        new
                        {
                            Id = 1,
                            DateOfPrediction = "2024-17-06",
                            DaysPredicted = 30,
                            PredictedReturn = 3.3399999999999999,
                            Ticker = "AAPL"
                        },
                        new
                        {
                            Id = 2,
                            DateOfPrediction = "2024-17-06",
                            DaysPredicted = 30,
                            PredictedReturn = -0.20999999999999999,
                            Ticker = "NVDA"
                        });
                });
#pragma warning restore 612, 618
        }
    }
}
